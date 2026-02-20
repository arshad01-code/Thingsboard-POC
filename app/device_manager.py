import json, time
from app.config import DEVICE_TOKENS, MAX_RETRIES
from app.mqtt_client import create_client
from app.telemetry import generate_telemetry
from app.retry import retry_execution

def send_device_data(token: str, device_index: int):
    device_name = f"Device-{device_index}"

    def publish():
        client = create_client(
            token=token
        )
        data = generate_telemetry(
            device_name=device_name
        )

        result = client.publish(
            topic="v1/devices/me/telemetry",
            payload=json.dumps(data),
            qos=1
        )

        result.wait_for_publish()
        print(f"SUCCESS: {device_name} -> {data}")
        client.disconnect()

    retry_execution(publish, MAX_RETRIES)

def run_all_devices():
    for index, token in enumerate(DEVICE_TOKENS, start=1):
        send_device_data(
            token=token,
            device_index=index
        )
        time.sleep(2)
