from pyramid.config import Configurator
from pyramid.response import Response

def main(global_config, **settings):
    """Pyramid main entry point."""
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')  
        config.add_static_view(name='static', path='myproject:static')
        config.add_route('home', '/')
        config.scan('.views')
    return config.make_wsgi_app()
