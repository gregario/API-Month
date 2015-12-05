# -*- coding: utf-8 -*-
# Find Local Air quality data in your area
# Greg Jackson 5st dev 2015
# Twitter @gr3gario or github gregario
# Day Five of the Month of API

import requests
import json 
import sys # needed to pass arguments from command line 

url = "http://api.erg.kcl.ac.uk/AirQuality/Information/MonitoringSites/GroupName=All/JSON" # Gives all units in London for AQ
q = requests.get(url).json() # Make a request to the TFL API for data
r = json.dumps(q)
print str(q['Sites']['Site'])
#aq = []
# So I'm going to make 4 lists, of name, sensor ID, lat, lng. I would be cleaner to make a list of JSON objects but screw it. 
#for key in r: # the returned object is a list with nested JSON objects inside each list. So you need to iterate through the list and do operations on each object separately
#ß	print key['Site']['@SiteCode'] # Adds expected arrival time from each train data structure to the time list

#print aq[0,1]
#print str(r['Sites']['@SiteCode'])