from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_api_add():
    response = client.post("/api/add", json={"a": 5.5, "b": 3.0})
    assert response.status_code == 200
    assert response.json() == {"a": 5.5, "b": 3.0, "result": 8.5}
