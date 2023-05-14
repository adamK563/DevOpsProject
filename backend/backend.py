<<<<<<< HEAD
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
=======
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
>>>>>>> 1731ba29a6fa2ceffc05c4c20ec8dccf5f0a8539
