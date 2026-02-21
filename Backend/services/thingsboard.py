import requests

def login(host, email, password):
    r = requests.post(
        f"{host}/api/auth/login",
        json={"username": email, "password": password}
    )
    r.raise_for_status()
    return r.json()["token"]

def create_dashboard(host, token, dashboard_json):
    headers = {"X-Authorization": f"Bearer {token}"}
    r = requests.post(
        f"{host}/api/dashboard",
        json=dashboard_json,
        headers=headers
    )
    r.raise_for_status()
    return r.json()