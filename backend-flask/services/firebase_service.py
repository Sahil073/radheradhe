"""
Firebase service
Handles sensor data (from ESP32) and command writing (to relays)
"""

import firebase_admin
from firebase_admin import credentials, db
from config import Config

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")  # Add your service account key
    firebase_admin.initialize_app(cred, {
        "databaseURL": Config.FIREBASE_DB_URL
    })

def get_sensor_data():
    """Fetch latest sensor data from Firebase"""
    ref = db.reference("sensors/")
    return ref.get()

def set_command(zone, command):
    """Send command (ON/OFF) to a zone via Firebase"""
    ref = db.reference(f"commands/{zone}")
    ref.set(command)
