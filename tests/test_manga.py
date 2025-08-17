from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
#you should add the "test" prefix to the function name
def test_manga_exists():
    response = client.get("/manga/Berserk")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

def test_manga_not_found():
    response = client.get("/manga/NoExiste")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) == 0
