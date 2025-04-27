import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user data status code:", create_user_response.status_code)
print("Create user data:", create_user_response_data)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post(url="http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print('Login data status code:', login_response.status_code)
print('Login data:', login_response_data)

patch_user_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
patch_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
patch_user_response = httpx.patch(
    f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=patch_user_headers,
    json=patch_user_payload
)

patch_user_response_data = patch_user_response.json()

print('Patch user data status code:', patch_user_response.status_code)
print('Patch user data:', patch_user_response_data)
