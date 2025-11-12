import pytest
from webtest import TestApp
from myproject import main

@pytest.fixture(scope="session")
def wsgi_app():
    settings = {'myproject.debug': True}
    app = main({}, **settings)
    return app

@pytest.fixture
def app(wsgi_app):
    return TestApp(wsgi_app)
