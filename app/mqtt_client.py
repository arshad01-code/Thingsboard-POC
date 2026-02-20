import paho.mqtt.client as mqtt
import ssl
from app.config import BROKER, PORT

def create_client(token: str) -> mqtt.Client:
    client = mqtt.Client()
    client.username_pw_set(token)

    # TLS encryption
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
    client.connect(
        host=BROKER, port=PORT, keepalive=60
    )
    return client
