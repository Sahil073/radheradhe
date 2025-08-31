"""
Scenario Controller
Applies rules/algorithms to control zones automatically
"""

from services.firebase_service import set_command

def apply_scenarios(sensor_data):
    """
    Auto-control zones based on rules:
    - If battery too low or output too high -> turn OFF
    - Else -> keep ON
    """
    for zone, values in sensor_data.items():
        battery_v = values.get("batteryVoltage", 0)
        input_p = values.get("inputPower", 0)
        output_p = values.get("outputPower", 0)

        if battery_v < 11.5 or output_p > input_p * 1.2:
            set_command(zone, "OFF")
        else:
            set_command(zone, "ON")
