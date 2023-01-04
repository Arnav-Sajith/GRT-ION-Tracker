import googlemaps
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from datetime import datetime



def Conestoga(gmaps, stop):
    directions = gmaps.directions(
        stop,
        mode="transit",
        departure_time=datetime.now(),
        destination="Conestoga Mall Station, Waterloo, Ontario, Canada",
        transit_mode = "rail"
    )
    return directions
# Request the next bus time for the specified stop and route

def Fairway(gmaps, stop):
    directions2 = gmaps.directions(
        stop,
        mode="transit",
        departure_time=datetime.now(),
        destination="Fairway Station, Waterloo, Ontario, Canada",
        transit_mode = "rail"
    )
    return directions2