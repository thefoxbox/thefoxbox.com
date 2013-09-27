""" WSGI Music Controller """

from base import BaseController
from views.music import MusicView

class MusicController(BaseController):
    def view(self, environ, start_response):
        view = MusicView()
        if hasattr(view, '__call__'):
            return view(environ)

