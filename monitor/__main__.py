import socketio
import eventlet
from monitor.monitor import MonitorNamespace
from monitor.cogitare import CogitareNamespace
from .execution import ExecutionsManager
from flask import Flask


sio = socketio.Server()
app = Flask(__name__)


manager = ExecutionsManager()

monitor = MonitorNamespace('/monitor')
cogitare = CogitareNamespace('/cogitare')

manager.monitor = monitor
manager.cogitare = cogitare

cogitare.manager = manager
monitor.manager = manager

sio.register_namespace(monitor)
sio.register_namespace(cogitare)

if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 8787)), app)
