import re
import httpx
import json

APP_URL = "http://localhost:3000"


def test_get_user():
    response = httpx.get(url=f"{APP_URL}/users")
    assert response.status_code == 200


def test_put_user():
    with open("put_payload.json") as f:
        put_payload = json.load(f)
    response = httpx.put(url=f"{APP_URL}/users/2", data=put_payload)
    assert response.status_code == 200


def test_patch_user():
    with open("patch_payload.json") as f:
        patch_payload = json.load(f)
    response = httpx.patch(url=f"{APP_URL}/users/1", data=patch_payload)
    assert response.status_code == 200


def test_create_user():
    with open("post_payload.json") as f:
        post_payload = json.load(f)
    response = httpx.post(url=f"{APP_URL}/users", data=post_payload)
    assert response.status_code == 201


def test_check_user_created():
    with open("post_payload.json") as f:
        post_payload = json.load(f)
    id_to_check = post_payload["id"]
    response = httpx.get(url=f"{APP_URL}/users").json()
    all_ids = [int(entry["id"]) for entry in response]
    assert id_to_check in all_ids


def test_delete_user():
    response = httpx.delete(url=f"{APP_URL}/users/100")
    assert response.status_code == 200
