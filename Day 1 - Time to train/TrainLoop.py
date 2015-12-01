# -*- coding: utf-8 -*-
### Program to check how long it will take me to get to work.
### Greg Jackson 1/12/15 
### Twitter @gr3gario | github gregario
### Day one of the Month of API

import requests
import json 
import time

while True: 
	url = "https://staging-developer.citymapper.com/api/1/traveltime/"
	payload = {'startcoord': '51.4618199,-0.1793686', 'endcoord': '51.560117,-0.0722408','time_type':'arrival','key':'INSERTKEY'}
	r = requests.get(url, params=payload).json()
	print(r['travel_time_minutes'])
	time.sleep(90)
