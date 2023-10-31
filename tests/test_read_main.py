from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_root_content():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.json().keys()
    assert response.json()["Hello"] == "World"



def test_read_nonexistent_endpoint():
    response = client.get("/nonexistent")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
