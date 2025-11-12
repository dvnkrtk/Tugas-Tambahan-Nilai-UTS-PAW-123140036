from webtest import TestApp
from myproject import main
import os

def make_app(settings=None):
    if settings is None:
        settings = {}
    return main({}, **settings)

def test_home_page_status_and_content():
    app = TestApp(make_app({'myproject.site_name': 'FunctionalTest'}))
    res = app.get('/') 
    assert res.status_code == 200
    assert 'FunctionalTest' in res.text
