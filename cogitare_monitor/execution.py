from unidecode import unidecode


class Execution(object):

    def __init__(self, name, description=None, machine=None, connected=False, save_on_disk=True,
                 usage=None):
        self.id = None
        self.name = name
        self.description = description
        self.machine = machine
        self.connected = connected
        self.save_on_disk = save_on_disk
        self.usage = usage
        self._usage_enabled = False
        self._sid = None
        self._plots = {}

    def get_dict(self, sid):
        d = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'machine': self.machine,
            'connected': self.connected,
            'save_on_disk': self.save_on_disk,
            'usage': self.usage,
            '_usage_enabled': self._usage_enabled,
            '_sid': self._sid,
            '_plots': dict()
        }

        for monitor_sid, monitor in self._plots.items():
            if monitor_sid != sid:
                continue
            for plot_name, plot in monitor.items():
                d['_plots'][plot_name] = plot.get_data(self.id)
            break

        print(d)
        return d

    def __str__(self):
        return str(self.get_dict())

    def get_plot_group(self, monitor_sid, group):
        self._plots.setdefault(monitor_sid, {})
        self._plots[monitor_sid].setdefault(group, {})

        return self._plots[monitor_sid][group]


class Manager(object):

    def __init__(self, cogitare, monitor):
        self.executions = {}
        self.monitors = set()

        cogitare.manager = self
        monitor.manager = self

        self.cogitare = cogitare
        self.monitor = monitor

    def execution_by_sid(self, sid):
        for execution in self.executions.values():
            if execution._sid == sid:
                return execution

    def _unique_id(self, name):
        name = unidecode(name.lower())
        keepcharacters = (' ', ',', '-', '_')
        name = ''.join(c for c in name if c.isalnum() or c in keepcharacters).strip()

        if name not in self.executions.keys():
            return name

        # add numeric value to generate new name
        new_name = name + '_1'
        idx = 2
        while name in self.executions.keys():
            new_name = name + '_' + str(idx)
            idx += 1

        return new_name

    def __iter__(self):
        for e in self.executions.values():
            yield e

    def append(self, execution):
        unique_id = self._unique_id(execution.name)
        execution.id = unique_id

        self.executions[unique_id] = execution

        self.monitor.add_execution(execution)

    def remove(self, execution):
        unique_id = execution.id
        if unique_id not in self.executions:
            return False

        del self.executions[unique_id]
        self.monitor.disconnect_execution(execution)

        # save and reload from log
        # if execution.save_on_disk:
        # name = self.save(execution)
        # self.monitor.remove_execution(execution)
        # self.load(name)
