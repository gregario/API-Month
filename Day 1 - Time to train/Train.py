### Program to check how long it will take me to get to work.
### Greg Jackson 1/12/15 
### Twitter @gr3gario | github gregario
### Day one of the Month of API

import requests
import json 

url = "https://staging-developer.citymapper.com/api/1/traveltime/"
payload = {'startcoord': '51.4988199,-0.1813686', 'endcoord': '51.560117,-0.0722408','time_type':'arrival','key':'INSERTKEYHERE'}
r = requests.get(url, params=payload).json()
print(r['travel_time_minutes'])
