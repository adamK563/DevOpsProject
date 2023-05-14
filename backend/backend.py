from fastapi import FastAPI
import requests

# Api object this will initialize our api
app = FastAPI()

# Check
@app.get("/")
def home():
    return {"message": "Welcome to our DevOps Project Backend! 😊"}

API_URL = "http://api.open-notify.org/iss-now.json" 

@app.get("/isslocation")
async def get_spacecraft_location():
    response = requests.get(API_URL)
    location = response.json()["iss_position"]
    return location
