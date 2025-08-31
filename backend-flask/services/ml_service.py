"""
Machine Learning service
Prediction + anomaly detection (basic stubs, expandable later)
"""

def predict_battery_sustain(battery_voltage, load):
    """
    Predict how many hours battery will sustain
    Simple stub formula: voltage * factor / load
    """
    if load == 0:
        return float("inf")
    hours = round((battery_voltage * 10) / load, 2)
    return hours

def detect_anomaly(expected, actual):
    """
    Detect anomaly if actual deviates >20% from expected
    """
    return abs(expected - actual) > expected * 0.2
