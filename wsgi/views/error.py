""" WSGI Error View """

import os
import pystache

templates = os.path.join(os.path.dirname(__file__), 'templates')

class ErrorView(object):
    def __call__(self):
        renderer = pystache.Renderer(search_dirs=templates)
        return renderer.render_name('error')

