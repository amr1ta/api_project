import requests

# GET method to fetch details
r = requests.get(url="http://localhost:3000/users")
print("GET method status, {}".format(r.status_code), r.text)

p = {"id": 1}
# GET method to fetch details with parameter
r = requests.get(url="http://localhost:3000/users", params=p)
print("GET method status, {}".format(r.status_code), r.text)


# write response from GET method in a file
r = requests.get(url="http://localhost:3000/users")
with open("get_response.json", "w+") as f:
    f.write(r.text)


# #PUT method
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
r = requests.put(url="http://localhost:3000/users/1", data=put_payload)
print("PUT method status, {} and response {} ".format(r.status_code, r.text))

r = requests.get(url="http://localhost:3000/users")
print("GET method status, {} and response {} ".format(r.status_code, r.text))


# #PATCH method to update particular entry

patch_payload = {"name": "Amardeep Kahali", "email": "amardeep.kahali@xyz.com"}
r = requests.patch(url="http://localhost:3000/users/1", data=patch_payload)
print("PATCH method status, {} and response {} ".format(r.status_code, r.text))

r = requests.get(url="http://localhost:3000/users")
print("GET method status, {} and response {} ".format(r.status_code, r.text))


# POST method to add a new entry
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
r = requests.post(url="http://localhost:3000/users", data=post_payload)
print("POST method status, {} and response {} ".format(r.status_code, r.text))

r = requests.get(url="http://localhost:3000/users")
print("GET method status, {} and response {} ".format(r.status_code, r.text))


# DELETE method
r = requests.delete(url="http://localhost:3000/users/100")
print("DELETE method status, {} ".format(r.status_code))

r = requests.get(url="http://localhost:3000/users")
print("GET method status, {} and response {} ".format(r.status_code, r.text))
