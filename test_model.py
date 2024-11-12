from fastapi.testclient import TestClient
from route import app

client = TestClient(app)

# для отладки
# import models
# models.create_db()


def test_create_theme():
    theme_data = {"name": "Test Theme", "text": "Test Description"}
    response = client.post("/theme/", json=theme_data)
    assert response.status_code == 200
    assert response.json()["name"] == theme_data["name"]

def test_create_comment():
    theme_data = {"name": "Test Theme", "text": "Test Description"}
    theme_response = client.post("/theme/", json=theme_data)
    theme_id = theme_response.json()["id"]
    comment_data = {"theme_id": theme_id, "author_name": "Test Author", "text": "Test Comment", "quote_id": -1}
    response = client.post(f"/comment/{theme_id}", json=comment_data)
    assert response.status_code == 200
    assert response.json()["theme_id"] == theme_id

def test_get_themes():
    response = client.get("/theme/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_theme():
    theme_data = {"name": "Test Theme", "text": "Test Description"}
    theme_response = client.post("/theme/", json=theme_data)
    theme_id = theme_response.json()["id"]
    response = client.get(f"/theme/{theme_id}")
    assert response.status_code == 200
    assert response.json()["id"] == theme_id

def test_get_comments():
    theme_data = {"name": "Test Theme", "text": "Test Description"}
    theme_response = client.post("/theme/", json=theme_data)
    theme_id = theme_response.json()["id"]
    response = client.get(f"/comment/{theme_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_comment():
    theme_data = {"name": "Test Theme", "text": "Test Description"}
    theme_response = client.post("/theme/", json=theme_data)
    theme_id = theme_response.json()["id"]
    comment_data = {"theme_id": theme_id, "author_name": "Test Author", "text": "Test Comment", "quote_id": -1}
    comment_response = client.post(f"/comment/{theme_id}", json=comment_data)
    comment_id = comment_response.json()["id"]
    response = client.get(f"/comment/{theme_id}/{comment_id}")
    assert response.status_code == 200
    assert response.json()["id"] == comment_id

def test_update_comment():
    theme_data = {"name": "Test Theme", "text": "Test Description"}
    theme_response = client.post("/theme/", json=theme_data)
    theme_id = theme_response.json()["id"]
    comment_data = {"theme_id": theme_id, "author_name": "Test Author", "text": "Test Comment", "quote_id": -1}
    comment_response = client.post(f"/comment/{theme_id}", json=comment_data)
    comment_id = comment_response.json()["id"]
    updated_comment_data = {"author_name": "Updated Author", "text": "Updated Comment", "quote_id": -1}
    # response = client.put(f"/comment/{theme_id}/{comment_id}/{updated_comment_data}", json=updated_comment_data)
    response = client.put(f"/comment/{theme_id}/{comment_id}", json=updated_comment_data)
    assert response.status_code == 200
    assert response.json()["author_name"] == updated_comment_data["author_name"]

def test_delete_theme():
    theme_data = {"name": "Test Theme", "text": "Test Description"}
    theme_response = client.post("/theme/", json=theme_data)
    theme_id = theme_response.json()["id"]
    response = client.delete(f"/theme/{theme_id}")
    assert response.status_code == 200
    assert response.json()["id"] == theme_id

# print(test_create_theme())
# print(test_create_comment())
# print(test_get_themes())
# print(test_get_theme())
# print(test_get_comments())
# print(test_get_comment())
# print(test_update_comment())
# print(test_delete_theme())