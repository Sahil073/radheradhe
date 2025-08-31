from flask import Blueprint
from controllers.household_controller import get_household_data
from core.decorators import token_required

household_bp = Blueprint("household", __name__)

@household_bp.route("/status", methods=["GET"])
@token_required(role="household")
def status(user_data):
    return get_household_data(user_data)
