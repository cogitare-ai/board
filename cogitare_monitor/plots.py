from bokeh.server.server import Server
from bokeh.application.application import Application
from threading import Thread


class BokehServer(Thread):

    def __init__(self):
        super(BokehServer, self).__init__(daemon=True)
        self._server = None

    def run(self):
        self._server = Server({'/': Application()}, num_procs=2, address='localhost', allow_websocket_origin=['*'])
        self._server.start()
        self._server.io_loop.start()
