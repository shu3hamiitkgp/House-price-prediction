from fastapi import FastAPI, Response, status
import utils
import requests
from pydantic import BaseModel

app = FastAPI()

class home_details(BaseModel):
    total_sqft: str
    location: str
    bath: str
    balcony: str
    bhk: str

@app.get('/get_location_names')
def get_location_names():
    location_list=utils.get_location_names()
    return {'Locations':location_list}

@app.post('/predict_home_price')
def predict_home_price(home_details:home_details):
    total_sqft = float(home_details.total_sqft)
    location = home_details.location
    balcony = int(home_details.balcony)
    bhk = int(home_details.bhk)
    bath = int(home_details.bath)
    
    home_price = utils.get_estimated_price(location,total_sqft,bhk,balcony,bath)
    
    return {'Estimated Price':home_price}