from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
import uvicorn

app = FastAPI(
    title="ENT Clinical Calculator API",
    description="Production-grade API for Otolaryngology calculations",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PTAInput(BaseModel):
    left_500: float = Field(ge=0, le=120)
    left_1000: float = Field(ge=0, le=120)
    left_2000: float = Field(ge=0, le=120)
    right_500: float = Field(ge=0, le=120)
    right_1000: float = Field(ge=0, le=120)
    right_2000: float = Field(ge=0, le=120)

class SNOT22Input(BaseModel):
    scores: List[int]

class StopBangInput(BaseModel):
    snoring: bool
    tired: bool
    observed_apnea: bool
    pressure: bool
    bmi: float
    age: int
    neck_circumference: float
    gender: str

@app.get("/")
def read_root():
    return {"status": "online", "system": "ENT Clinical Calculator Suite"}

@app.post("/calculate/pta")
def calculate_pta(data: PTAInput):
    left_avg = (data.left_500 + data.left_1000 + data.left_2000) / 3
    right_avg = (data.right_500 + data.right_1000 + data.right_2000) / 3
    
    def classify(avg):
        if avg <= 25: return "Normal Hearing"
        if avg <= 40: return "Mild Hearing Loss"
        if avg <= 60: return "Moderate Hearing Loss"
        if avg <= 80: return "Severe Hearing Loss"
        return "Profound Hearing Loss"
    
    return {
        "left_ear_avg": round(left_avg, 2),
        "right_ear_avg": round(right_avg, 2),
        "classification": classify(max(left_avg, right_avg))
    }

@app.post("/calculate/snot22")
def calculate_snot22(data: SNOT22Input):
    total = sum(data.scores)
    severity = "None/Minimal"
    if total > 20: severity = "Mild"
    if total > 40: severity = "Moderate"
    if total > 60: severity = "Severe"
    return {"total_score": total, "severity": severity, "max_score": 110}

@app.post("/calculate/stopbang")
def calculate_stopbang(data: StopBangInput):
    score = 0
    if data.snoring: score += 1
    if data.tired: score += 1
    if data.observed_apnea: score += 1
    if data.pressure: score += 1
    if data.bmi > 35: score += 1
    if data.age > 50: score += 1
    if data.neck_circumference > 40: score += 1
    if data.gender == "male": score += 1
    
    risk = "Low Risk"
    if score >= 3: risk = "Intermediate Risk"
    if score >= 5: risk = "High Risk"
    
    return {"score": score, "risk_category": risk, "max_score": 8}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
