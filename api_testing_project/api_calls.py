
#related third party imports
import httpx
import json

class Api_Calls:
    
    def get_method(self, url):
        self.url = url
        r = httpx.get(self.url)
        r_response = json.loads(r.text)
        with open ("get_response.json", "w+") as f:
            f. write(r.text)
        return r.status_code, r_response, r.headers['content-type']


    def put_method(self, url):
        self.url = url
        r = httpx.get(self.url)
        r_response = json.loads(r.text)
        with open ("get_response.json", "w+") as f:
            f. write(r.text)
        return r.status_code, r_response, r.headers['content-type']



a = Api_Calls()
print (a.get_method(url="http://localhost:3000/users"))

