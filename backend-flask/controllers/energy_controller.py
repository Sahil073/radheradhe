"""
Energy Controller
Handles battery stats, anomaly detection
"""

from flask import jsonify
from services.firebase_service import get_sensor_data
from services.ml_service import predict_battery_sustain, detect_anomaly

def energy_status():
    """Return overall energy status, battery sustain time, anomalies"""
    data = get_sensor_data()
    if not data:
        return jsonify({"message": "No data available"}), 404

    # For demo, pick Zone1 (can be looped for all zones later)
    zone = "Zone1"
    input_p = data[zone].get("inputPower", 0)
    output_p = data[zone].get("outputPower", 0)
    battery_v = data[zone].get("batteryVoltage", 0)

    sustain_time = predict_battery_sustain(battery_v, output_p)
    anomaly = detect_anomaly(input_p, output_p)

    return jsonify({
        "raw": data,
        "batterySustainHours": sustain_time,
        "anomalyDetected": anomaly
    })
