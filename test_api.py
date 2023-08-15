import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_days(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Monday' in response.data

def test_get_day(client):
    response = client.get('/3')
    assert response.status_code == 200
    assert b'Wednesday' in response.data

def test_get_invalid_day(client):
    response = client.get('/10')
    assert response.status_code == 404

def test_post_days(client):
    response = client.post('/')
    assert response.status_code == 201
    assert b'success' in response.data


