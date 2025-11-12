from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPBadRequest

@view_config(route_name='home', renderer='string')
def home_view(request):
    return "Welcome to MyProject - open /hello/yourname or /search?q=term"

@view_config(route_name='hello_name', renderer='string')
def hello_name_view(request):
    name = request.matchdict.get('name', 'stranger')
    return f"Hello, {name}!"

@view_config(route_name='search', renderer='string')
def search_view(request):
    q = request.params.get('q')
    if not q:
        return "Please provide ?q=..."
    return f"Search results for: {q}"

@view_config(route_name='submit', renderer='string', request_method='GET')
def submit_form(request):
    return """
    <form method="post" action="/submit">
      <input name="username" placeholder="username"/>
      <input type="submit" value="Send"/>
    </form>
    """

@view_config(route_name='submit', request_method='POST')
def submit_handler(request):
    username = request.POST.get('username')
    if not username:
        raise HTTPBadRequest("username required")

    return HTTPFound(location=request.route_url('hello_name', name=username))

@view_config(route_name='api_echo', renderer='json')
def api_echo(request):
    try:
        data = request.json_body
    except Exception:
        data = {}
    return {"echo": data}

@view_defaults(renderer='string')
class GreetingViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='hello_name', request_method='GET', decorator=None)
    def greet_via_class(self):
        name = self.request.matchdict.get('name', 'stranger')
        return f"[class view] Hello, {name}"
