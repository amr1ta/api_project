import api_client
import pytest
import json


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost:3000")
    parser.addoption("--username", action="store", default="default_username")
    parser.addoption("--password", action="store", default="default_password")


@pytest.fixture(scope="class")
def apiclient(pytestconfig):
    url = pytestconfig.getoption("url")
    username = pytestconfig.getoption("username")
    password = pytestconfig.getoption("password")
    return api_client.Api_Client(url, username, password)


@pytest.fixture()
def employee_data():
    with open("post_payload.json") as f:
        return json.load(f)
