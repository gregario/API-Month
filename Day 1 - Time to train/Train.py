import requests
import json 

#startLat  = 51.4988199 
#startLong = -0.1813686
#finLat    = 51.560117
#finLong   = -0.0722408
#cityKey = 'a49adfbd011e30ef98f776fb4175c931'

#url = "https://staging-developer.citymapper.com/api/1/traveltime/?startcoord=%d %2C %d&endcoord=%d%2C%d&time_type=arrival&key=%s" % (startLat, startLong, finLat, finLong)
#print url


#All you need to get the raw output of a command Install requests if you don't have it (sudo easy_install requests) using citymapper requests. Import requests and use below
# Documentation http://docs.python-requests.org/en/latest/user/quickstart/ 
# sign up to use citymapper API here
# API documentation here: traveltime
# where did I get lat long. Gmaps 

r = requests.get ("https://staging-developer.citymapper.com/api/1/traveltime/?startcoord=51.4988199%2C-0.1813686&endcoord=51.560117%2C-0.0722408&time_type=arrival&key=a49adfbd011e30ef98f776fb4175c931")
#print(r.json())

#Output looks like this 
# {u'travel_time_minutes': 54, u'diagnostic': {u'milliseconds': 2907}} 

#But output is JSON so you need to handle that too import JSON
#once you are playing with JSON you need to be able to parse JSON. Its easy but this tutorial helps. Basically turns jSON into a dict and all those rules then apply
#http://docs.python-guide.org/en/latest/scenarios/json/
url = "https://staging-developer.citymapper.com/api/1/traveltime/?startcoord=51.4988199%2C-0.1813686&endcoord=51.560117%2C-0.0722408&time_type=arrival&key=a49adfbd011e30ef98f776fb4175c931"

r=requests.get(url).json()
#r_parsed = json.loads(r)
print(r['travel_time_minutes'])
#print (json.dumps(r))
#print(r_parsed(travel_time_minutes))


#n = json.dumps(m)  
#o = json.loads(n)  
#print o['id'], o['name']
#print(parsed_json['first_name'])