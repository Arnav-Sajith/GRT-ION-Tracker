from get_directions import Conestoga, Fairway
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


app = QApplication([])
window = QWidget()
window.setWindowFlag(Qt.FramelessWindowHint)
window.setStyleSheet("background-color: transparent;")
conestoga_times = ''.join(str(x) for x in Conestoga())
label1 = QLabel("The Next ION to Conestoga arrives at " + conestoga_times)
label1.setStyleSheet("font-size: 24px; color: white; background-color: #1E90FF; border-radius: 10px; padding: 10px;")
label2 = QLabel("The Next ION to Fairway arrives at " + Fairway())
label2.setStyleSheet("font-size: 24px; color: white; background-color: #1E90FF; border-radius: 10px; padding: 10px;")
layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
window.setLayout(layout)
window.show()
app.exec_()