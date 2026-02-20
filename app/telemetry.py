import random

def generate_telemetry(device_name: str) -> dict:
    return {
        "device_name": device_name,
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "vibration": round(random.uniform(0, 10), 2),
    }