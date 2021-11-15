from app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert b"Hello, World!" in response.data
