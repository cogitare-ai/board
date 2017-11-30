import re
from bokeh.plotting import curdoc, figure
from bokeh.client import push_session
from bokeh.embed import server_session
from bokeh.models import ColumnDataSource
time = 0


class Plot:

    def __init__(self, title, data=None):
        self._title = title
        tools = 'save'
        self._p = figure(title=title, x_axis_type=None, sizing_mode='stretch_both', tools=tools)
        self._p.x_range.follow = 'end'
        self._p.x_range.follow_interval = 100
        self._p.x_range.range_padding = 0

        self.data = data or {}
        self.source = ColumnDataSource(data=self.data)
        self._script = None

    def add_variable(self, name):
        self._p.line(x='x', y=name, source=self.source)

    def _create_plot(self):
        curdoc().add_root(self._p)
        session = push_session(curdoc(), session_id='usage')
        script = server_session(self._p, session_id=session.id)

        self._script = script

    def __str__(self):
        if self._script is None:
            self._create_plot()
        return self._script

    def stream(self, data, rollover=None):
        self.source.stream(data, rollover=rollover)

    def get_data(self, execution_id):
        script = str(self).strip()

        plot_src = re.findall(r' src="(.*?)"', script)[0]
        model_id = re.findall(r' data-bokeh-model-id="(.*?)"', script)[0]
        plot_id = re.findall(r' id="(.*?)"', script)[0]

        return {'id': execution_id, 'name': self._title,
                'plot_src': plot_src, 'plot_id': plot_id,
                'plot_model_id': model_id}


def on_toggle_system_usage(manager, sid, execution_id):
    execution = manager.executions[execution_id]
    execution._plots.clear()
    manager.cogitare.emit('toggle_system_usage', room=execution._sid)


def _get_data(time, value):
    if isinstance(value, dict):
        data = dict((x, [y]) for x, y in value.items())
    else:
        data = {'y': [value]}

    data['x'] = [time]

    return data


def on_update_usage(manager, sid, usage):
    global time
    time += 1
    execution = manager.execution_by_sid(sid)

    for key, value in usage.items():

        for monitor in manager.monitors:
            data = _get_data(time, value)
            plot_holder = execution.get_plot_group(monitor, 'usage')
            if key not in plot_holder:
                plot = Plot(key, data)
                for variable in data.keys():
                    if variable == 'x':
                        continue
                    plot.add_variable(variable)

                plot_holder[key] = plot
                manager.monitor.emit('add_usage_plot', plot.get_data(execution.id), monitor)
            else:
                plot_holder[key].stream(data, 100)


PLUG = {
    'name': 'System Usage',
    'view': '',
    'monitor': {
        'toggle_system_usage': on_toggle_system_usage
    },
    'cogitare': {
        'update_usage': on_update_usage
    }
}


__all__ = ['PLUG']
