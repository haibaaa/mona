# mona/config.py
import os
from dotenv import load_dotenv

load_dotenv()


CONFIG_API = os.environ.get("LISA_CONFIG_API")
SERVER_URL = os.environ.get("LISA_SERVER_URL", "https://lisa-aopa.onrender.com")


def validate():
    if not CONFIG_API:
        raise EnvironmentError("LISA_CONFIG_API is not set in your .env file")
