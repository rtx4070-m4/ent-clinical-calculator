def calculate_stopbang(params):
    score = 0
    if params.get('snoring'): score += 1
    if params.get('tired'): score += 1
    if params.get('observed_apnea'): score += 1
    if params.get('pressure'): score += 1
    if params.get('bmi', 0) > 35: score += 1
    if params.get('age', 0) > 50: score += 1
    if params.get('neck_circumference', 0) > 40: score += 1
    if params.get('gender') == 'male': score += 1
    return {"score": score}
