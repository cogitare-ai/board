import socketio
from cogitare_monitor.execution import Execution


class CogitareNamespace(socketio.Namespace):

    def __init__(self, name):
        super(CogitareNamespace, self).__init__(name)
        self.manager = None

    def on_disconnect(self, sid):
        execution = self.manager.execution_by_sid(sid)
        if execution:
            self.manager.remove(execution)

    def on_register(self, sid, data):
        execution = Execution(**data)
        execution.connected = True
        execution._sid = sid
        self.manager.append(execution)
