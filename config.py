import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

ENV = bool(os.environ.get("ENV", False))

if ENV or os.path.exists(".env"):
    from sample_config import *  # noqa
elif os.path.exists("config.py"):
    from config import *

# Define the Config class with the API_ID, API_HASH, and BOT_TOKEN attributes
class Config:
    API_ID = os.environ.get('API_ID')
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
