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

    def create_device(self, device_name, customer_id, type):
        headers = {
            "X-Authorization": f"Bearer {self.token}"
        }
        response = requests.post(
            f"{TB_URL}/api/device",
            headers=headers,
            json={
                "name": device_name,
                "type": type,
                "customerId": {
                    "id": str(customer_id),
                    "entityType": "CUSTOMER"
                }
            }
        )
        device = response.json()

        device_id = device["id"]["id"]
        device_type = device["type"]

        cred = requests.get(
            f"{TB_URL}/api/device/{device_id}/credentials",
            headers=headers
        )

        token = cred.json()["credentialsId"]
        print(cred.json())

        return device_id, device_type, token
    
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
    
    def create_tb_customer(self, customer_name, email):

        headers = {
            "X-Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        payload = {
            "title": customer_name,
            "email": email
        }

        response = requests.post(
            f"{TB_URL}/api/customer",
            headers=headers,
            json=payload
        )
        print(response.json())
        return response.json()["id"]["id"]
    
    def get_device(self):
        headers = {
            "X-Authorization": f"Bearer {self.token}"
        }
        response = requests.get(
            f"{TB_URL}/api/device/{"952c8b00-1992-11f1-8f13-7592a37a10f8"}",
            headers=headers
        )
        device = response.json()

        print(device)
    
    def send_telemetry(token, data):

        url = f"{TB_URL}/api/v1/{token}/telemetry"
        requests.post(url, json=data)