"""
Notification system (SMS via Twilio)
"""

from twilio.rest import Client
from config import Config

def send_sms(to, message):
    """Send SMS notification using Twilio"""
    client = Client(Config.TWILIO_SID, Config.TWILIO_AUTH)
    client.messages.create(
        to=to,
        from_=Config.TWILIO_PHONE,
        body=message
    )
