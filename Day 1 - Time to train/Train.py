import requests
import json 

#startLat  = 51.4988199 
#startLong = -0.1813686
#finLat    = 51.560117
#finLong   = -0.0722408
#cityKey = 'a49adfbd011e30ef98f776fb4175c931'

#url = "https://staging-developer.citymapper.com/api/1/traveltime/?startcoord=%d %2C %d&endcoord=%d%2C%d&time_type=arrival&key=%s" % (startLat, startLong, finLat, finLong)
#print url

r = requests.get ("https://staging-developer.citymapper.com/api/1/traveltime/?startcoord=51.4988199%2C-0.1813686&endcoord=51.560117%2C-0.0722408&time_type=arrival&key=a49adfbd011e30ef98f776fb4175c931")
#r.json()
#print r
#json.dump(r)
print(r.json())