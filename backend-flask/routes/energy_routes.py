from flask import Blueprint
from controllers.energy_controller import energy_status

energy_bp = Blueprint("energy", __name__)

@energy_bp.route("/status", methods=["GET"])
def status():
    return energy_status()
