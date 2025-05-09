import httpx
from tools.fakers import fake

user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=user_payload)
response_data = response.json()

print(response.status_code)
print(response_data)
