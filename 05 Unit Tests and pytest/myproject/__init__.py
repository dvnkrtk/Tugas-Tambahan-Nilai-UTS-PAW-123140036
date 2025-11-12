from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_view('myproject.views.home_view', route_name='home')
    return config.make_wsgi_app()
