import requests
from config import TB_URL, TB_USERNAME, TB_PASSWORD

class ThingsBoardClient():

    def __init__(self):
        self.token = self.authenticate()

    def authenticate(self):
        response = requests.post(
            f"{TB_URL}/api/auth/login",
            json={
                "username": TB_USERNAME,
                "password": TB_PASSWORD
            }
        )
        # print("LOGIN RESPONSE", response.json())
        return response.json()["token"]

    def create_device(self, device_name):
        headers = {
            "X-Authorization": f"Bearer {self.token}"
        }
        response = requests.post(
            f"{TB_URL}/api/device",
            headers=headers,
            json={
                "name": device_name,
                "type": "Industrial Sensor"
            }
        )
        print("DEVICE CREATE STATUS:", response.status_code)
        print("DEVICE CREATE RESPONSE:", response.text)
        return response.json()["id"]["id"], response.json()["type"]
    
    def create_dashboard(self, dashboard_name):
        headers = {
            "X-Authorization": f"Bearer {self.token}"
        }
        response = requests.post(
            f"{TB_URL}/api/dashboard",
            headers=headers,
            json={
                "title": dashboard_name
            }
        )
        print("DASHBOARD CREATE STATUS:", response.status_code)
        print("DASHBOARD CREATE RESPONSE:", response.text)
        return response.json()
    
    def create_tb_customer(self, customer_name):

        headers = {
            "X-Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        payload = {
            "title": customer_name
        }

        response = requests.post(
            f"{TB_URL}/api/customer",
            headers=headers,
            json=payload
        )
        # print(response.json())
        return response.json()["id"]["id"]