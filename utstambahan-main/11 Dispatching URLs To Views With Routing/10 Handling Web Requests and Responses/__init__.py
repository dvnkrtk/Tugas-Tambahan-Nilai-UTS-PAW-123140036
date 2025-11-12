from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    config.add_route('home', '/')
    config.add_route('greet', '/greet/{name}')
    config.add_route('form', '/form')
    
    config.scan('.views')
    return config.make_wsgi_app()
