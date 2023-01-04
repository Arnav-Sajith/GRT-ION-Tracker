import os
import googlemaps
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

# Loads Environmental Variables
load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")
ION_STOP = os.environ.get("ION_STOP")

# Create a Google Maps Client object with your API key
gmaps = googlemaps.Client(key=API_KEY)
stop = ION_STOP


# Request the next bus time for the specified stop and route
def Conestoga():
    directions = gmaps.directions(
        stop,
        mode="transit",
        departure_time=datetime.now(),
        destination="Conestoga Mall Station, Waterloo, Ontario, Canada",
        transit_mode = "rail"
    )
    return directions[0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"]
# Request the next bus time for the specified stop and route

def Fairway():
    directions2 = gmaps.directions(
        stop,
        mode="transit",
        departure_time=datetime.now(),
        destination="Fairway Station, Waterloo, Ontario, Canada",
        transit_mode = "rail"
    )
    return directions2[0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"]