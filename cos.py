#!/usr/bin/env python

# Colorado Springs Airport Flight Status, --Harold Wilson, Sept. 2018 

import sys

try:
  import requests
except Exception as e:
   sys.stderr.write("ERROR -- Unablle to import the 'requests' site package.\n")
   sys.stderr.write("         try: pip install request\n\n")
   sys.exit(1)

URL = "https://www.infax.com/webfids/cos/fids-cos.json"

try:
   r = requests.get(URL)
except Exception as e:
   sys.stderr.write("ERROR -- Unablle to access '%s'.\n" %URL)
   sys.stderr.write("         Check your Internet connection..\n")
   sys.exit(2)

def display_flights(flight_data, direction):
   flight_type = direction[0].upper()
   print "*** %s ***" % direction
   print "       CITY      |      Flight      | Time  | Gate |  Ramarks"
   print "-----------------+------------------+-------+------+---------------"
   for flight in flight_data['flights']['flight']:
      if flight['type'] == flight_type:
         print "%-16s | %-10s %-5s | %s:%s | %-4s |  %s" %(flight['city']     ,
                                                          flight['an']        ,
                                                          flight['flt']       ,
                                                          flight['sked'][0:2] ,
                                                          flight['sked'][2:4] ,
                                                          flight['gate']      ,
                                                          flight['rem']       )
   print "--------------------------------------------------------------------"

if  r.status_code == requests.codes.ok:

   json_flight_data = r.json()

   display_flights(json_flight_data, "Arriving")
   print ""
   display_flights(json_flight_data, "Departing")

else:

   sys.stderr.write("ERROR -- Unable to retrieve data from '%s'.\n" %URL)
   sys.stderr.write("         Response: %d.\n" %r.status_code)
   sys.exit(3)

sys.exit(0)


