import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_pta_calculation():
    payload = {
        "left_500": 25, "left_1000": 30, "left_2000": 35,
        "right_500": 28, "right_1000": 32, "right_2000": 38
    }
    response = client.post("/calculate/pta", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "left_ear_avg" in data
    assert "right_ear_avg" in data

def test_stopbang_calculation():
    payload = {
        "snoring": True, "tired": True, "observed_apnea": False,
        "pressure": False, "bmi": 32, "age": 45,
        "neck_circumference": 38, "gender": "male"
    }
    response = client.post("/calculate/stopbang", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
