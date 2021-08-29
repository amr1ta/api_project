import api_client
import pytest

apiclient = api_client.Api_Client(url="http://localhost:3000/users")

class Test_Users_Api:
    def test_get_all_users(self):
        status_code, _ = apiclient.get_all_users()
        assert status_code == 200

    @pytest.mark.parametrize("user_id", [1, 3, 4])
    def test_get_valid_user_by_id(self, user_id):
        status_code, _ = apiclient.get_user_by_id(user_id)
        assert status_code == 200

    @pytest.mark.parametrize("user_id", [20, 30, 40])
    def test_get_invalid_user_by_id(self, user_id):
        status_code, _ = apiclient.get_user_by_id(user_id)
        assert status_code == 404

    def test_create_user(self, user_data):
        status_code, response = apiclient.create_user(user_data)
        assert status_code == 201
        Test_Users_Api._created_user_id = response["id"]

    def test_delete_user(self):
        status_code = apiclient.delete_user(Test_Users_Api._created_user_id)
        assert status_code == 200
