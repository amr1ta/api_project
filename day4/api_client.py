import requests


class Api_Client:
    def __init__(self, url, username, password):
        self._url = url
        self.session = requests.Session()
        access_token = self.get_bearer_token(username, password)
        self.session.headers.update({"Authorization": access_token})

    def get_bearer_token(self, email, password):
        login_payload = {}
        login_payload["email"] = email
        login_payload["password"] = password
        r = self.session.post(url=f"{self._url}/login", data=login_payload)
        if r.status_code == 200:
            return f"Bearer {r.json()['accessToken']}"

    def get_all_employees(self):
        r = self.session.get(url=f"{self._url}/employees")
        return r.status_code, r.json()

    def get_employee_by_id(self, employee_id):
        r = self.session.get(url=f"{self._url}/employees/{employee_id}")
        return r.status_code, r.json()

    def create_employee(self, employee_payload):
        r = self.session.post(url=f"{self._url}/employees", data=employee_payload)
        if r.status_code == 201:
            return r.status_code, r.json()
        return r.status_code, r.text

    def delete_employee(self, employee_id):
        r = self.session.delete(url=f"{self._url}/employees/{employee_id}")
        return r.status_code
