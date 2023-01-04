# Import the necessary modules
import googlemaps
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout



# Create a QApplication object to manage the GUI
app = QApplication([])

# Create a QWidget to hold the GUI elements
class MyWidget(QWidget):
    # Override the QWidget's mousePressEvent() method to handle mouse press events
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    # Override the QWidget's mouseMoveEvent() method to handle mouse move events
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

# Create a QWidget to hold the GUI elements
window = QWidget()

# Set the window to be frameless
window.setWindowFlag(Qt.FramelessWindowHint)

# Set the background color of the window to transparent
window.setStyleSheet("background-color: transparent;")

# Create a QLabel to display the next bus time
label1 = QLabel("The Next ION to Conestoga arrive at " + directions[0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"])

# Set the font, color, and background of the label
label1.setStyleSheet("font-size: 24px; color: white; background-color: #1E90FF; border-radius: 10px; padding: 10px;")

# Create a QLabel to display the next bus time
label2 = QLabel("The Next ION to Fairway arrive at " + directions2[0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"])

# Set the font, color, and background of the label
label2.setStyleSheet("font-size: 24px; color: white; background-color: #1E90FF; border-radius: 10px; padding: 10px;")

# Create a layout to hold the labels
layout = QVBoxLayout()

# Add the labels to the layout
layout.addWidget(label1)
layout.addWidget(label2)

# Set the layout of the window to the layout we created
window.setLayout(layout)


# Show the window
window.show()

# Run the QApplication
app.exec_()