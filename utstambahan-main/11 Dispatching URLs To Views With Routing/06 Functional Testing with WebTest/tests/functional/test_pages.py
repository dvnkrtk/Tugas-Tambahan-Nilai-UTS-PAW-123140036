def test_home_page(app):
    res = app.get('/', status=200)
    assert b"<h1>Home</h1>" in res.body
