import os
import googlemaps
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
from arcgis.gis import GIS


# Loads Environmental Variables
load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")
ION_STOP = os.environ.get("ION_STOP")
STATION_ID = os.environ.get("STATION_ID")
# Create a Google Maps Client object with your API key
gmaps = googlemaps.Client(key=API_KEY)
stop = ION_STOP

def list_of_stops():
    gis = GIS()
    ion_stop_file = gis.content.get(STATION_ID)
    ion_stop_file
    ion_stop_file.download(save_path=os.getcwd())

# Request the next bus time for the specified stop and route
def Conestoga(current_location):
    directions = gmaps.directions(
        stop,
        alternatives = True,
        mode="transit",
        destination="Conestoga Mall Station, Waterloo, Ontario, Canada",
        transit_mode = "rail"
    )
    departure_time = find_departure_times(directions)
    return departure_time
# Request the next bus time for the specified stop and route


def check_transit_availability(directions_result):
    for route in directions_result:
        for leg in route['legs']:
            for step in leg['steps']:
                if step['travel_mode'] == 'TRANSIT':
                    return True
    return False

def find_departure_times(data):
    # This list will hold all found departure times
    departure_times = []
    
    # If the current piece of data is a dictionary
    if isinstance(data, dict):
        # If 'transit_details' is in the dictionary and 'departure_time' is in 'transit_details'
        if 'transit_details' in data and 'departure_time' in data['transit_details']:
            vehicle_info = data['transit_details']['line']['vehicle']
            vehicle_type = vehicle_info.get('name', '')
            # Check if the vehicle type is "HEAVY_RAIL" or another keyword that indicates a train
            if vehicle_type.lower() == 'train':
                departure_time = data['transit_details']['departure_time']['text']
                departure_times.append(departure_time)
        # Recursively search through the dictionary
        for value in data.values():
            departure_times.extend(find_departure_times(value))
    
    # If the current piece of data is a list
    elif isinstance(data, list):
        # Recursively search through each item in the list
        for item in data:
            departure_times.extend(find_departure_times(item))
    return departure_times

def Fairway():
    directions2 = gmaps.directions(
        stop,
        mode="transit",
        departure_time=datetime.now(),
        destination="Fairway Station, Waterloo, Ontario, Canada",
        transit_mode = "rail"
    )
    # print(directions2)
    return directions2[0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"]