""" WSGI Music View """

import os
import markdown
import pystache
from cStringIO import StringIO
from webob import Request

content = os.path.join(os.path.dirname(__file__), '../../public_html/content')
templates = os.path.join(os.path.dirname(__file__), 'templates')

class MusicView(object):
    """Read markdown file and render template."""
    def __call__(self, environ):
        html = ''
        req = Request(environ)
        filename, ext = os.path.splitext(req.path_info)
        markdown_file = content + filename + '.md' 
        media_file = filename + '.mp3'
        if os.path.isfile(markdown_file):
            _buffer = StringIO()
            md = markdown.markdownFromFile(input=markdown_file, output=_buffer)
            html = _buffer.getvalue()
            _buffer.close()
        renderer = pystache.Renderer(search_dirs=templates)
        return renderer.render_name('music', {'content': html, 'media': media_file})

