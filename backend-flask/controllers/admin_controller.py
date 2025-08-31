"""
Admin Controller
Admin can control zones (ON/OFF)
"""

from flask import request, jsonify
from services.firebase_service import set_command
from core.logger import log_action

def control_zone(user, zone, action):
    """Allow admin to switch a zone ON/OFF"""
    if action not in ["ON", "OFF"]:
        return jsonify({"message": "Invalid action"}), 400
    
    set_command(zone, action)
    log_action(user["id"], f"Set {zone} to {action}", zone)
    return jsonify({"message": f"Zone {zone} set to {action}"})
