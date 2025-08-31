"""
Household Controller
Allows household to check their own data
"""

from flask import jsonify
from services.firebase_service import get_sensor_data

def get_household_data(user):
    """Fetch energy data for household based on ID"""
    data = get_sensor_data()
    return jsonify({"yourData": data.get(user.get("householdId"), {})})
