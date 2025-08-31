from flask import Blueprint, request
from controllers.admin_controller import control_zone
from core.decorators import token_required

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/control", methods=["POST"])
@token_required(role="admin")
def control(user_data):
    data = request.json
    return control_zone(user_data, data.get("zone"), data.get("action"))
