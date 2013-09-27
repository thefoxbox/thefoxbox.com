""" WSGI Error Controller """

from webob import Response
from base import BaseController
from views.error import ErrorView

class ErrorController(BaseController):
    def not_found(self, *args):
        view = ErrorView()
        if hasattr(view, '__call__'):
            return view()

