"""
Handles JWT authentication: generating & decoding tokens
"""

import jwt, datetime
from flask import current_app

def generate_token(user):
    """Generate JWT token for a user with expiry of 12 hours"""
    payload = {
        "id": user["id"],
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

def decode_token(token):
    """Decode JWT token and return payload if valid"""
    try:
        return jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
    except:
        return None
