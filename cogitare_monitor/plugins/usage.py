import re
from bokeh.models import HoverTool
from bokeh.plotting import curdoc, figure
from bokeh.client import push_session
from bokeh.embed import server_session
from bokeh.models import ColumnDataSource
from bokeh.models import PrintfTickFormatter
from bokeh.palettes import Spectral
import itertools
time = 0
colors = itertools.cycle(Spectral[9])


class Plot:

    def __init__(self, title, data=None):
        self._title = title
        tools = 'save'
        self._p = figure(title=title, x_axis_type=None, sizing_mode='stretch_both', tools=tools)
        self._p.yaxis.axis_label = title
        self._p.yaxis[0].formatter = PrintfTickFormatter(format='%7.2f')
        self._p.x_range.follow = 'end'
        self._p.x_range.follow_interval = 100
        self._p.x_range.range_padding = 0

        self.data = data or {}
        self.source = ColumnDataSource(data=self.data)
        self._script = None
        self._last_line = None
        self.tooltips = []

    def add_variable(self, name):
        color = next(colors)
        self._last_line = self._p.line(x='x', y=name, source=self.source, line_width=2, line_alpha=0.8,
                                       legend=' ' + name, line_color=color, muted_alpha=0.2, muted_color=color)
        self._p.circle(x='x', y=name, source=self.source, legend=' ' + name, fill_color=None, line_color=color,
                       muted_alpha=0.3, muted_color=color)

        self.tooltips.append((name, '@{' + name + '}{%7.2f}'))

    def _create_plot(self):
        curdoc().add_root(self._p)
        session = push_session(curdoc(), session_id='usage')
        script = server_session(self._p, session_id=session.id)

        self._script = script

    def __str__(self):
        if self._script is None:
            self._p.legend.orientation = "horizontal"
            self._p.legend.location = "top_left"
            self._p.legend.background_fill_alpha = 0.8
            self._p.legend.click_policy = "mute"

            formatters = dict((name, 'printf') for name, _ in self.tooltips)

            self._p.add_tools(HoverTool(
                renderers=[self._last_line],
                tooltips=self.tooltips,
                mode='vline',
                formatters=formatters))
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
