def calculate_dhi(scores):
    total = sum(scores)
    severity = "No Handicap"
    if total > 30: severity = "Mild"
    if total > 48: severity = "Moderate"
    if total > 58: severity = "Severe"
    return {"total": total, "severity": severity}

def calculate_vor_gain(eye_velocity, head_velocity):
    if head_velocity == 0:
        return 0.0
    return eye_velocity / head_velocity
