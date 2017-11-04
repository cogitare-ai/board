import socketio
import logging
import coloredlogs
import functools
from ..execution import Execution


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())
coloredlogs.install(level='INFO', logger=LOGGER)


def with_execution(func):

    @functools.wraps(func)
    def f(self, sid, *args, **kwargs):
        execution = self._executions[sid]
        return func(self, execution, sid, *args, **kwargs)

    return f


class CogitareNamespace(socketio.Namespace):

    def __init__(self, *args, **kwargs):
        super(CogitareNamespace, self).__init__(*args, **kwargs)
        self._executions = {}
        self.manager = None

    def on_connect(self, sid, env):
        LOGGER.info('Cogitare client connected with ID {}'.format(sid))
        self._executions[sid] = Execution()

    def on_disconnect(self, sid):
        LOGGER.info('Cogitare client with ID {} disconnected'.format(sid))
        self.manager.remove(self._executions[sid])
        del self._executions[sid]

    @with_execution
    def on_register(self, execution, sid, data):
        LOGGER.info('Cogitare {} registered with name="{}" and description="{}"'
                    .format(sid, data['name'], data['description']))

        execution.name = data['name']
        execution.desc = data['description']
        execution.connected = True
        execution.save_on_disk = data['save_on_disk']

        self.manager.append(execution)

    @with_execution
    def on_machine(self, execution, sid, machine):
        LOGGER.info('Registed Cogite client\'s machine')
        execution.machine = machine
