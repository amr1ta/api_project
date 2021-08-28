import httpx


class Api_Calls:

    def __init__(self, url):
        self._url = url

    def get_method(self):
        r = httpx.get(self._url)
        with open ("get_response.json", "w+") as f:
            f. write(r.text)
        return r.status_code, r.json(), r.headers['content-type']

    def put_method(self, param, payload):
        self._param = param
        r = httpx.put(self._url+self._param, data = payload)
        with open ("put_response.json", "w+") as f:
            f. write(r.text)
        return r.status_code, r.json(), r.headers['content-type']

    def patch_method(self, param, payload):
        self._param = param
        r = httpx.patch(self._url+self._param, data = payload)
        with open ("patch_response.json", "w+") as f:
            f. write(r.text)
        return r.status_code, r.json(), r.headers['content-type']

    def post_method(self, payload):
        r = httpx.post(self._url, data = payload)
        with open ("post_response.json", "w+") as f:
            f. write(r.text)
        return r.status_code, r.json(), r.headers['content-type']

    def delete_method(self, param ):
        r = httpx.delete(self._url+param)
        return r.status_code, r.headers['content-type']



a = Api_Calls(url="http://localhost:3000/users")
put_payload = {
    "name": "Amrita Mahapatra",
    "username": "gugu",
    "email": "amrita.mahapatra@xyz.com",
    "address": {
        "street": "9th cross Layout",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {"lat": "-37.3159", "lng": "81.1496"},
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets",
    },
}

patch_payload = {"name": "Amardeep Kahali", "email": "amardeep.kahali@xyz.com"}

post_payload = {
    "id": 100,
    "name": "Amrita Mahapatra",
    "username": "tester",
    "email": "amrita.mahapatra@xyz.com",
    "address": {
        "street": "9th cross Layout",
        "suite": "Apt. 556",
        "city": "BAngalore",
        "zipcode": "560001",
        "geo": {"lat": "12.3113", "lng": "40.1496"},
    },
    "phone": "1-770-736-8031 x56442",
    "website": "apitesting.org",
    "company": {
        "name": "ABB",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets",
    },
}

print (a.get_method())
print (a.put_method(param="/2", payload=put_payload))
print (a.post_method(payload=post_payload))
print (a.patch_method(param="/1", payload=patch_payload))
print (a.delete_method(param="/100"))