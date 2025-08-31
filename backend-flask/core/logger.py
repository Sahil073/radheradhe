"""
Audit logging system
Keeps track of who performed what action (useful for judges + debugging)
"""

import datetime

def log_action(user_id, action, zone=None):
    """Log actions like zone ON/OFF, alerts, etc."""
    with open("audit.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - User {user_id} performed {action} on {zone}\n")
