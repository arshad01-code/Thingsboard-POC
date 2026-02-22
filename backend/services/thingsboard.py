import requests
from config import TB_URL, TB_USERNAME, TB_PASSWORD

_tb_token = None

def get_token():
    global _tb_token

    if _tb_token:
        return _tb_token

    response = requests.post(
        f"{TB_URL}/api/auth/login",
        json={
            "username": TB_USERNAME,
            "password": TB_PASSWORD
        }
    )
    response.raise_for_status()
    _tb_token = response.json()["token"]
    return _tb_token


def tb_request(method, endpoint, json=None):
    token = get_token()
    headers = {"X-Authorization": f"Bearer {token}"}

    response = requests.request(
        method,
        f"{TB_URL}{endpoint}",
        headers=headers,
        json=json
    )

    response.raise_for_status()
    return response.json()