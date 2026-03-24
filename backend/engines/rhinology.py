def calculate_snot22(scores):
    total = sum(scores)
    severity = "None/Minimal"
    if total > 20: severity = "Mild"
    if total > 40: severity = "Moderate"
    if total > 60: severity = "Severe"
    return {"total": total, "severity": severity}
