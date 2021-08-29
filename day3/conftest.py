import pytest
import json

@pytest.fixture()
def user_data():
    with open("post_payload.json") as f:
            user_payload = json.load(f)
    return user_payload