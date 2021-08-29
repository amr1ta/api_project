import api_client
import pytest


@pytest.fixture(scope="session")
def apiclient():
    print("Logging in")
    return api_client.Api_Client("http://localhost:3000", "amrita@mail.com", "P@ssw0rd")


class Test_Users_Api:

    def test_get_all_employees(self, apiclient):
        status_code, _ = apiclient.get_all_employees()
        assert status_code == 200

    @pytest.mark.parametrize("employee_id", [1, 3, 4])
    def test_get_valid_employee_by_id(self, employee_id, apiclient):
        status_code, _ = apiclient.get_employee_by_id(employee_id)
        assert status_code == 200

    @pytest.mark.parametrize("employee_id", [20, 30, 40])
    def test_get_invalid_employee_by_id(self, employee_id, apiclient):
        status_code, _ = apiclient.get_employee_by_id(employee_id)
        assert status_code == 404

    def test_create_employee(self, employee_data, apiclient):
        status_code, response = apiclient.create_employee(employee_data)
        assert status_code == 201
        Test_Users_Api._created_employee_id = response["id"]

    def test_delete_employee(self, apiclient):
        status_code = apiclient.delete_employee(
            Test_Users_Api._created_employee_id
        )
        assert status_code == 200
