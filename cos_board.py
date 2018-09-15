#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys

try:
  import requests
except Exception as e:
   sys.stderr.write("ERROR -- Unablle to import the 'requests' site package.\n")
   sys.stderr.write("         try: pip install request\n\n")
   sys.exit(1)

URL = "https://www.infax.com/webfids/cos/fids-cos.jsonQQQQQQ"

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QErrorMessage
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

URL =  "https://www.infax.com/webfids/cos/fids-cos.json"

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Welcome to the Colorado Springs Airport'
        self.left = 100
        self.top = 50
        self.width = 800
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

        try:
            r = requests.get(urlqweqweq)
        except Exception as e:
            QMessageBox().error(self, 
                                "No Flight Data", 
                                "Unable to retrieve flight data.", 
                                QMessageBox.Critical)
 

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(800,500)
        print("-")
        



        # Add tabs
        self.tabs.addTab(self.tab1,"Arriving")
        self.tabs.addTab(self.tab2,"Departing")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.tableArriving = QTableWidget()
        self.tableArriving.setRowCount(0)
        self.tableArriving.setColumnCount(5)
        self.tableArriving.setHorizontalHeaderLabels("City;Flight;Time;Gate;Remarks".split(";"))
        self.tab1.layout.addWidget(self.tableArriving)
        self.tab1.setLayout(self.tab1.layout)

        # Create Second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tableDeparting = QTableWidget()
        self.tableDeparting.setRowCount(0)
        self.tableDeparting.setColumnCount(5)
        self.tableDeparting.setHorizontalHeaderLabels("City;Flight;Time;Gate;Remarks".split(";"))

        self.tab2.layout.addWidget(self.tableDeparting)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    def get_flight_data(self, url):
        json_flight_data = {}
    
        return json_flight_data



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
