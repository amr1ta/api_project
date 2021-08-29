import pytest
import json


@pytest.fixture()
def employee_data():
    with open("post_payload.json") as f:
        return json.load(f)
