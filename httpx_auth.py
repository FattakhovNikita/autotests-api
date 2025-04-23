import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

headers = {"Authorization": "Bearer"}
with httpx.Client(headers=headers, base_url="http://127.0.0.1:8000/api/v1/") as client:
    login_response = client.post(url="authentication/login", json=login_payload)
    login_response_data = login_response.json()

    refresh_payload = {
        "refreshToken": login_response.json()['token']['refreshToken']
    }

    refresh_response = client.post(url="authentication/refresh", json=refresh_payload)

print("Login response", login_response_data)
print("Login response status", login_response.status_code)
print()
print("Refresh response", refresh_response.json())
print("Refresh response code", refresh_response.status_code)
