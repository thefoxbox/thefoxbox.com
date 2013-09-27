""" WSGI Article Controller """

from webob import Response
from base import BaseController
from views.article import ArticleView

class ArticleController(BaseController):
    def view(self, environ, start_response):
        view = ArticleView()
        if hasattr(view, '__call__'):
            return view(environ)

