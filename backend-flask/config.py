"""
Configuration file for Flask backend
Keeps all API keys, database URLs, and secrets in one place
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")   # Used for JWT auth
    FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL", "")       # Firebase DB URL
    TWILIO_SID = os.getenv("TWILIO_SID", "")
    TWILIO_AUTH = os.getenv("TWILIO_AUTH", "")
    TWILIO_PHONE = os.getenv("TWILIO_PHONE", "")
