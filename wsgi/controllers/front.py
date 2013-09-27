""" WSGI Front Controller """

from base import BaseController
from views.front import FrontView

class FrontController(BaseController):
    def index(self, *args):
        view = FrontView()
        if hasattr(view, '__call__'):
            return view()

