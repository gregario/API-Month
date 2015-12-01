### Program to check how long it will take me to get to work using the citymapper API
### Greg Jackson 1/12/15 
### Twitter @gr3gario | github gregario
### Day one of the Month of API

import requests
import json 


## All you need to get the raw output of a command Install requests if you don't have it (sudo easy_install requests) using citymapper requests. Import requests and use below
## Documentation http://docs.python-requests.org/en/latest/user/quickstart/ 
## sign up to use citymapper API here. https://content.citymapper.com/i/897/citymapper-for-developers 
## API documentation here: traveltime
## where did I get lat long. Google maps!

#r = requests.get ("https://staging-developer.citymapper.com/api/1/traveltime/?startcoord=51.4988199%2C-0.1813686&endcoord=51.560117%2C-0.0722408&time_type=arrival&key=[INSERTKEYHERE]")
#print(r.json())

## Output looks like this 
## {u'travel_time_minutes': 54, u'diagnostic': {u'milliseconds': 2907}} 

## But output is JSON so you need to handle that too by adding "import JSON"
## once you are playing with JSON you need to be able to parse JSON. Its easy but this tutorial helps. Basically turns jSON into a dict and all those rules then apply
## http://docs.python-guide.org/en/latest/scenarios/json/
#url = "https://staging-developer.citymapper.com/api/1/traveltime/?startcoord=51.4988199%2C-0.1813686&endcoord=51.560117%2C-0.0722408&time_type=arrival&key=[INSERTKEYHERE]"
#r=requests.get(url).json()
#print(r['travel_time_minutes'])

# Finally I want to make this a little more user friendly by including the payload as a separate variable. 
# This way you can make changes easily or include this as a function in a larger program or load the start/end coordinates from a file
url = "https://staging-developer.citymapper.com/api/1/traveltime/"
payload = {'startcoord': '51.4988199,-0.1813686', 'endcoord': '51.560117,-0.0722408','time_type':'arrival','key':'INSERTKEYHERE'}
r = requests.get(url, params=payload).json()
print(r['travel_time_minutes'])
