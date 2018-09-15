#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Colorado Springs Airport FLight Information, Harold Wilson, Spet. 2018
# Note the program does not update ... yet.
# Saving realtime updates for version 2.0

import sys

try:
  import requests
except:
   sys.stderr.write("ERROR -- Unablle to import the 'requests' site package.\n")
   sys.stderr.write("         try: pip install request\n\n")
   sys.exit(1)

try:
   from PyQt5.QtWidgets import QMainWindow, QApplication
   from PyQt5.QtWidgets import QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
   from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
   from PyQt5.QtWidgets import QMessageBox, QErrorMessage, QAbstractScrollArea
   from PyQt5.QtGui import QIcon
   from PyQt5.QtCore import pyqtSlot
except:
   sys.stderr.write("ERROR -- Unablle to import the 'pyqt5' site package.\n")
   sys.stderr.write("         try: pip install pyqt5\n\n")
   sys.exit(2)

URL =  "https://www.infax.com/webfids/cos/fids-cos.json"

class App(QMainWindow):

    def __init__(self): 

        # Initialise the Main Window       
        super().__init__()
        self.title = 'Welcome to the Colorado Springs Airport'
        self.left = 100
        self.top = 50
        self.width = 600
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
      
        # Initialize tabs widget
        self.tabs = QTabWidget()
        self.tabArriving = QWidget()
        self.tabDeparting = QWidget()
        self.tabs.resize(800,500)
 
        # Add Arriving and Departing tabs to the tabs widget 
        self.tabs.addTab(self.tabArriving,"Arriving")
        self.tabs.addTab(self.tabDeparting,"Departing")

        # Create Arriving table
        self.tabArriving.layout = QVBoxLayout(self)
        self.tableArriving = QTableWidget()
        self.tableArriving.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableArriving.setRowCount(0)
        self.tableArriving.setColumnCount(5)
        self.tableArriving.setHorizontalHeaderLabels("City;Flight;Time;Bag;Remarks".split(";"))
        self.tabArriving.layout.addWidget(self.tableArriving)
        self.tabArriving.setLayout(self.tabArriving.layout)

        # Create Departing table
        self.tabDeparting.layout = QVBoxLayout(self)
        self.tableDeparting = QTableWidget()
        self.tableDeparting.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableDeparting.setRowCount(0)
        self.tableDeparting.setColumnCount(5)
        self.tableDeparting.setHorizontalHeaderLabels("City;Flight;Time;Gate;Remarks".split(";"))
        self.tabDeparting.layout.addWidget(self.tableDeparting)
        self.tabDeparting.setLayout(self.tabDeparting.layout)

        # Add tabs to the Main Window as the "Central Widget"
        self.setCentralWidget(self.tabs)
        
        # Paint the Main Window on the screen 
        self.show() # BANG!!!
        
        # Get the flight data from the server or present meaningful error message 
        try: 
            r = requests.get(URL)
            if  r.status_code == requests.codes.ok:
               json_flight_data = r.json()
            else:
               raise Exception("HTTP Error", str(r.status_code))
        except Exception as e:
            QMessageBox.critical(self, 
                                 'Critical Error', 
                                 "Unable to retrieve flight data.\n%s" %str(e))
            sys.exit(3)

        # Use the flight data to populate the tables
        arriving_flight_type  = 'A' # 
        departing_flight_type = 'D' #
        arriving_row_index    =  0  #
        departing_row_index   =  0  #

        # Size the table for "Arriving" Flights
        for flight in json_flight_data['flights']['flight']:
           if flight['type'] == arriving_flight_type:
              arriving_row_index +=1 
              self.tableArriving.setRowCount(arriving_row_index)

        arriving_row_index    =  0  #

        # Populate "Arriving" flights table
        for flight in json_flight_data['flights']['flight']:
           if flight['type'] == arriving_flight_type:
               
              self.tableArriving.setItem(arriving_row_index, 0, QTableWidgetItem(flight['city']  ))
              self.tableArriving.setItem(arriving_row_index, 1, QTableWidgetItem(flight['an'] + " " + flight['flt'] ))
              self.tableArriving.setItem(arriving_row_index, 2, QTableWidgetItem(flight['sked'][0:2] + ":" + flight['sked'][2:4]))
              self.tableArriving.setItem(arriving_row_index, 3, QTableWidgetItem(flight['bag']))
              self.tableArriving.setItem(arriving_row_index, 4, QTableWidgetItem(flight['rem']))
              arriving_row_index +=1
        self.tableArriving.resizeColumnsToContents()

        # Size the table for "Departing" Flights
        for flight in json_flight_data['flights']['flight']:
           if flight['type'] == departing_flight_type:
              departing_row_index +=1 
              self.tableDeparting.setRowCount(departing_row_index)        

        departing_row_index    =  0  #

        # Populate "Departing" flights table
        for flight in json_flight_data['flights']['flight']:
           if flight['type'] == departing_flight_type:
              self.tableDeparting.setItem(departing_row_index ,0, QTableWidgetItem(flight['city']  ))
              self.tableDeparting.setItem(departing_row_index ,1, QTableWidgetItem(flight['an'] + " " + flight['flt'] ))
              self.tableDeparting.setItem(departing_row_index ,2, QTableWidgetItem(flight['sked'][0:2] + ":" + flight['sked'][2:4]))
              self.tableDeparting.setItem(departing_row_index ,3, QTableWidgetItem(flight['gate']))
              self.tableDeparting.setItem(departing_row_index ,4, QTableWidgetItem(flight['rem']))
              departing_row_index +=1 
        self.tableDeparting.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
