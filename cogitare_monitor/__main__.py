import socketio
import eventlet
from cogitare_monitor.monitor import MonitorNamespace
from cogitare_monitor.cogitare import CogitareNamespace
from cogitare_monitor.execution import Manager
from flask import Flask
from cogitare_monitor.plots import BokehServer
from cogitare_monitor.plugins.machine import PLUG as MACHINE
from cogitare_monitor.plugins.usage import PLUG as USAGE
from cogitare_monitor.utils import assert_valid_plugin

sio = socketio.Server()
app = Flask(__name__)
bokeh_server = BokehServer()
bokeh_server.start()


monitor = MonitorNamespace('/monitor')
cogitare = CogitareNamespace('/cogitare')
manager = Manager(cogitare, monitor)

sio.register_namespace(monitor)
sio.register_namespace(cogitare)


def handler_for(func):
    def f(*args, **kwargs):
        return func(manager, *args, **kwargs)

    return f


PLUGINS = [MACHINE, USAGE]

for plugin in PLUGINS:
    assert_valid_plugin(plugin)
    for channel in ['monitor', 'cogitare']:
        for name, hook in plugin[channel].items():
            sio.on(name, handler_for(hook), '/' + channel)


if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 8787)), app)
