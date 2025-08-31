"""
Emergency alert system
"""

from services.notification_service import send_sms

def alert_emergency(contact_number, issue):
    """Send emergency alert to admin/authority"""
    message = f"⚠️ Emergency Alert: {issue}. Immediate action required."
    send_sms(contact_number, message)
