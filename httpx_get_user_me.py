import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

access_token = login_response_data['token']['accessToken']
auth_headers = {'Authorization': f'Bearer {access_token}'}

print("Login response", login_response_data)
print("Login response status", login_response.status_code)
print()

me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=auth_headers)
me_response_data = me_response.json()

print("Me response", me_response_data)
print("Me response status", me_response.status_code)
