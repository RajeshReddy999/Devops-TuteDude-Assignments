from types import SimpleNamespace

from app import create_app


class FakeCollection:
    def __init__(self, error=None):
        self.error = error
        self.documents = []

    def insert_one(self, document):
        if self.error:
            raise self.error
        self.documents.append(document)
        return SimpleNamespace(inserted_id="test-id")


def test_api_returns_list_from_backend_file():
    client = create_app(FakeCollection()).test_client()
    response = client.get("/api")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_submit_inserts_valid_data():
    collection = FakeCollection()
    client = create_app(collection).test_client()
    response = client.post("/submit", json={"name": "Asha", "email": "asha@example.com", "course": "DevOps"})
    assert response.status_code == 201
    assert collection.documents[0]["course"] == "DevOps"


def test_submit_returns_database_error_without_crashing():
    client = create_app(FakeCollection(RuntimeError("Atlas unavailable"))).test_client()
    response = client.post("/submit", json={"name": "Asha", "email": "asha@example.com", "course": "DevOps"})
    assert response.status_code == 500
    assert "Atlas unavailable" in response.get_json()["error"]
