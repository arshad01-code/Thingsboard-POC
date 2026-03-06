import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

url = "postgresql+psycopg2://thingsboard_poc_user:NiiILlWAhbMFjUuHe7kTXhPmfTo1DxVw@dpg-d6d16jtm5p6s73f3lif0-a.singapore-postgres.render.com/thingsboard_poc"
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

try:
    conn = engine.connect()
    print("✅ Connected successfully to database")
    conn.close()
except Exception as e:
    print("❌ Connection failed")
    print(e)