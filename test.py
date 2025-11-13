import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["message"].startswith("Hello")
