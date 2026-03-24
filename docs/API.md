# API Documentation

## Base URL
http://localhost:8000

## Endpoints

### GET /
Health check endpoint.

### POST /calculate/pta
Calculate Pure Tone Average.

**Body:**
```json
{
  "left_500": 20,
  "left_1000": 25,
  "left_2000": 30,
  "right_500": 22,
  "right_1000": 28,
  "right_2000": 32
}
```

### POST /calculate/snot22
Calculate SNOT-22 Score.

### POST /calculate/stopbang
Calculate STOP-BANG Score.
