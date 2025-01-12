from fastapi.testclient import TestClient
from app.main import app

# TODO: Write a test for the /analyze/ endpoint
client = TestClient(app)

def test_analyze_endpoint():
    response = client.post("/analyze/", json={
        "devpost_url": "https://example.com/devpost",
        "github_url": "https://github.com/example/repo"
    })
    assert response.status_code == 200
    assert "title" in response.json()
    assert "total_score" in response.json()