from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_jinja2")

    config.add_route("home", "/")
    config.add_route("hello_name", "/hello/{name}")
    config.add_route("search", "/search")
    config.add_route("submit", "/submit")
    config.add_route("api_echo", "/api/echo")

    config.scan("myproject")  

    return config.make_wsgi_app()
