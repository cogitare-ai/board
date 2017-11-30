import socketio
import logging
import coloredlogs


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())
coloredlogs.install(level='INFO', logger=LOGGER)


class MonitorNamespace(socketio.Namespace):

    def __init__(self, *args, **kwargs):
        super(MonitorNamespace, self).__init__(*args, **kwargs)
        self.manager = None

    def on_connect(self, sid, env):
        LOGGER.info('Monitor connected with ID {}'.format(sid))
        self.manager.monitors.add(sid)
        for execution in self.manager:
            self.add_execution(execution, sid)

    def on_disconnect(self, sid):
        if sid in self.manager.monitors:
            self.manager.monitors.remove(sid)
        LOGGER.info('Monitor with ID {} disconnected'.format(sid))

    def add_execution(self, execution, sid=None):
        self.emit('add_execution', execution.get_dict(sid), sid)

    def remove_execution(self, execution):
        self.emit('remove_execution', execution.id)

    def disconnect_execution(self, execution):
        self.emit('disconnect_execution', execution.id)

    def update_machine(self, execution, attr, machine):
        self.emit('update_machine', {'id': execution.id, 'machine': machine})
