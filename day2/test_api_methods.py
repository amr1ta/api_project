import api_client
import json

apiclient = api_client.Api_Client(url="http://localhost:3000/users")


class Test_Users_Api:
    def test_get_all_users(self):
        status_code, _ = apiclient.get_all_users()
        assert status_code == 200

    def test_get_user_by_id(self):
        status_code, _ = apiclient.get_user_by_id(3)
        assert status_code == 200

    def test_create_user(self):
        with open("post_payload.json") as f:
            user_payload = json.load(f)
        status_code, response = apiclient.create_user(user_payload)
        assert status_code == 201
        Test_Users_Api._created_user_id = response['id']

    def test_delete_user(self):
        status_code = apiclient.delete_user(Test_Users_Api._created_user_id)
        assert status_code == 200
