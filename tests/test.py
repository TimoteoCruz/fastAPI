from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_manga_found():
    response = client.get("/manga/Berserk")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    manga = data["data"][0]
    assert "title" in manga
