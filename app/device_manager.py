import json, time
import requests
from app.config import DEVICE_TOKENS, MAX_RETRIES, BROKER
from app.mqtt_client import create_client
from app.telemetry import generate_telemetry
from app.retry import retry_execution

def send_device_data(token: str, device_index: int):
    device_name = f"Device-{device_index}"

    """
    def publish():
        client = create_client(
            token=token
        )
        data = generate_telemetry(
            device_name=device_name
        )

        print("Sending payload:", data)
        result = client.publish(
            topic="v1/devices/me/telemetry",
            payload=json.dumps(data),
            qos=1
        )
        print("Waiting for publish")

        result.wait_for_publish()
        print(f"SUCCESS: {device_name} -> {data}")
        client.disconnect()
        print("Finished.")
    """    

    def publish(device_name, token):
        url = f"https://{BROKER}/api/v1/{token}/telemetry"
        data = generate_telemetry(
            device_name=device_name
        )
        print(f"{device_name}: Sending payload {data}", flush=True)
        try:
            response = requests.post(url, json=data, timeout=10)
            if response.status_code == 200:
                print(f"{device_name}: SUCCESS -> {data} (HTTP 200)", flush=True)
            else:
                print(f"{device_name}: FAILED -> {data} (HTTP {response.status_code})", flush=True)
        except Exception as e:
            print(f"{device_name}: ERROR -> {e}", flush=True)

    retry_execution(publish, MAX_RETRIES)

def run_all_devices():
    for index, token in enumerate(DEVICE_TOKENS, start=1):
        send_device_data(
            token=token,
            device_index=index
        )
        time.sleep(2)
