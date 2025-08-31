"""
Custom decorators for role-based access control
"""

from functools import wraps
from flask import request, jsonify
from core.auth import decode_token

def token_required(role=None):
    """
    Decorator to check if a valid JWT token is present.
    Optionally checks user role (admin/household).
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify({"message": "Token missing!"}), 403
            
            data = decode_token(token)
            if not data:
                return jsonify({"message": "Invalid or expired token!"}), 403
            
            if role and data["role"] != role:
                return jsonify({"message": "Access denied"}), 403
            
            return f(data, *args, **kwargs)
        return wrapper
    return decorator
