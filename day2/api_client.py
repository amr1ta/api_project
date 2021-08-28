import httpx


class Api_Client:
    def __init__(self, url):
        self._url = url

    def get_all_users(self):
        r = httpx.get(self._url)
        return r.status_code, r.json()

    def get_user_by_id(self, user_id):
        r = httpx.get(url=f"{self._url}/{user_id}")
        return r.status_code, r.json()

    def create_user(self, user_payload):
        r = httpx.post(self._url, data=user_payload)
        if r.status_code == 201:
            return r.status_code, r.json()
        return r.status_code, r.text

    def delete_user(self, user_id):
        r = httpx.delete(url=f"{self._url}/{user_id}")
        return r.status_code
