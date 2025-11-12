from pyramid.view import view_config

@view_config(route_name='hello_t', renderer='myproject:templates/hello.jinja2')
def hello_template(request):
    return {"name": "Devina", "site": request.registry.settings.get("myproject.site_name", "My Project")}
