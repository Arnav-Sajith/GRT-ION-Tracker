import googlemaps
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from get_directions import Conestoga, Fairway



load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")
ION_STOP = os.environ.get("ION_STOP")

# Create a Google Maps Client object with your API key
gmaps = googlemaps.Client(key=API_KEY)
# Define the stop and route to get the ION time for
stop = ION_STOP
route = "Ion"
# Get the current time
now = datetime.now()
# Request the next bus time for the specified stop and route

directions1 = Conestoga(gmaps, stop)
directions2 = Fairway(gmaps, stop)