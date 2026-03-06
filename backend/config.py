import os
from dotenv import load_dotenv

load_dotenv()

TB_URL = os.getenv("TB_URL")
TB_USERNAME = os.getenv("TB_USERNAME")
TB_PASSWORD = os.getenv("TB_PASSWORD")