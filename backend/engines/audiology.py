def calculate_pta(inputs):
    left_freqs = [inputs['left_500'], inputs['left_1000'], inputs['left_2000']]
    right_freqs = [inputs['right_500'], inputs['right_1000'], inputs['right_2000']]
    left_avg = sum(left_freqs) / 3
    right_avg = sum(right_freqs) / 3
    
    def classify(avg):
        if avg <= 25: return "Normal Hearing"
        if avg <= 40: return "Mild Hearing Loss"
        if avg <= 60: return "Moderate Hearing Loss"
        if avg <= 80: return "Severe Hearing Loss"
        return "Profound Hearing Loss"
    
    return {
        "left_ear_avg": round(left_avg, 2),
        "right_ear_avg": round(right_avg, 2),
        "classification": classify(max(left_avg, right_avg)),
        "raw_data": inputs
    }
