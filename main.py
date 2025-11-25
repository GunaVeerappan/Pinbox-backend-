from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Pinbox backend is running!"}
