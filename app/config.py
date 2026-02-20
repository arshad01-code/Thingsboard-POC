import os

BROKER = "thingsboard.cloud"
PORT = 8883
MAX_RETRIES = 5

DEVICE_TOKENS = [
    os.environ.get("DEVICE_1_TOKEN"),
    # os.environ.get("DEVICE_2_TOKEN"),
    # os.environ.get("DEVICE_3_TOKEN"),
]

DEVICE_TOKENS = [token for token in DEVICE_TOKENS if token]