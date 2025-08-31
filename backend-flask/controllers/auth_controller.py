"""
Authentication Controller
Handles login requests
"""

from flask import request, jsonify
from core.auth import generate_token

# Dummy user database (replace with Firebase Auth / DB later)
users = {
    "admin@urjalink.com": {"id": "1", "password": "admin123", "role": "admin"},
    "house1@urjalink.com": {"id": "2", "password": "house123", "role": "household", "householdId": "H001"}
}

def login():
    """Login API - validates user & returns JWT"""
    data = request.json
    email, password = data.get("email"), data.get("password")
    user = users.get(email)

    if user and user["password"] == password:
        token = generate_token(user)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401
