from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Pinbox backend is running",
        "status": "success"
    }


# ------- News Endpoint (Later you will connect real news API) -------
@app.get("/news")
def get_news():
    return {
        "topic": "news",
        "data": [
            {"title": "News item 1", "impact": "high"},
            {"title": "News item 2", "impact": "medium"},
            {"title": "News item 3", "impact": "low"}
        ]
    }


# ------- Economic Calendar Endpoint -------
@app.get("/calendar")
def get_calendar():
    return {
        "topic": "calendar",
        "events": [
            {"time": "10:30 AM", "event": "GDP Data", "impact": "high"},
            {"time": "12:00 PM", "event": "CPI Report", "impact": "medium"},
            {"time": "02:15 PM", "event": "Market Update", "impact": "low"}
        ]
    }


# ------- Alerts Endpoint -------
@app.get("/alerts")
def get_alerts():
    return {
        "topic": "alerts",
        "alerts": [
            {"title": "Price Alert Triggered"},
            {"title": "Trend Alert Activated"}
        ]
    }


# ------- Table Endpoint -------
@app.get("/table")
def get_table():
    return {
        "topic": "table",
        "rows": [
            {"pair": "EUR/USD", "value": 1.086},
            {"pair": "GBP/USD", "value": 1.243},
            {"pair": "USD/JPY", "value": 149.20}
        ]
    }
