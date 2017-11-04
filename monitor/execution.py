class Execution(object):

    def __init__(self):
        self.id = None
        self.name = None
        self.desc = None
        self.machine = None
        self.connected = False
        self.save_on_disk = True

    def get_dict(self):
        return self.__dict__


class ExecutionsManager(object):

    def __init__(self):
        self._executions = []
        self._ids = []
        self.cogitare = None
        self.monitor = None

    def _unique_id(self, name):
        keepcharacters = (' ', ',', '-', '_')
        name = ''.join(c for c in name if c.isalnum() or c in keepcharacters).strip()

        if name not in self._ids:
            return name

        # add numeric value to generate new name
        new_name = name + '_1'
        idx = 2
        while name in self._ids:
            new_name = name + '_' + str(idx)
            idx += 1

        return new_name

    def __iter__(self):
        for e in self._executions:
            yield e

    def append(self, execution):
        unique_id = self._unique_id(execution.name)
        execution.id = unique_id

        self._executions.append(execution)
        self._ids.append(unique_id)

        self.monitor.add_execution(execution)

    def load(self, name):
        pass

    def save(self, execution):
        pass

    def remove(self, execution):
        unique_id = execution.id
        self._ids.remove(unique_id)
        self._executions.remove(execution)
        self.monitor.disconnect_execution(execution)

        # save and reload from log
        # if execution.save_on_disk:
        # name = self.save(execution)
        # self.monitor.remove_execution(execution)
        # self.load(name)
