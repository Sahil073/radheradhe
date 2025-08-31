from flask import Blueprint
from controllers.scenario_controller import apply_scenarios
from services.firebase_service import get_sensor_data
from core.decorators import token_required

scenario_bp = Blueprint("scenario", __name__)

@scenario_bp.route("/apply", methods=["POST"])
@token_required(role="admin")
def apply(user_data):
    data = get_sensor_data()
    apply_scenarios(data)
    return {"message": "Scenario applied successfully"}
