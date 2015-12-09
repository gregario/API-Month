#coding: utf-8
# Day nine of the month of API
# Today finds your nearest petrol station, this one is less london-y 
# Greg Jackson @gr3gario on twitter and gregario on github

import requests
import json 
import sys  
import googlemaps
from APIKEY import googlekey


def addtoGPS():
	attempts = 0
	latlng = []
	addressInput = raw_input("where are you? ")	
	
	while attempts < 3:
		try:
			gmaps = googlemaps.Client(key=googlekey) # Get key from your google developer portal. 
			# Geocoding an address
			geocode_result = gmaps.geocode(addressInput) # passes address given on command line to google maps geocoding api
			
			for key in geocode_result: # the returned object is a list with nested JSON objects inside each list. So you need to iterate through the list and do operations on each object separately
				latlng.append(float(key['geometry']['bounds']['northeast']['lat'])) # pulls out nested latitude figure from call
				latlng.append(float(key['geometry']['bounds']['northeast']['lng'])) # pulls out nested longditude figure from call
			break
		
		except:
			attempts += 1
			print "Error getting data from Google maps API"	
	
	return latlng

def placefromGPS():
	attempts = 0
	
	
	while attempts < 3:
		try:
			gmaps = googlemaps.Client(key=googlekey) # Get key from your google developer portal. 
			# Geocoding an address
			geocode_result = gmaps.geocode(addressInput) # passes address given on command line to google maps geocoding api
			
			for key in geocode_result: # the returned object is a list with nested JSON objects inside each list. So you need to iterate through the list and do operations on each object separately
				latlng.append(float(key['geometry']['bounds']['northeast']['lat'])) # pulls out nested latitude figure from call
				latlng.append(float(key['geometry']['bounds']['northeast']['lng'])) # pulls out nested longditude figure from call
			break
		
		except:
			attempts += 1
			print "Error getting data from Google maps API"	
	
	return latlng


def placefromGPS():
	attempts = 0 
	radius = 3000 #in meters
	types = "gas_station" # these are predefined
	latlng = addtoGPS()
	address = []
	url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(latlng[0])+","+str(latlng[1])+"&radius="+str(radius)+"&types="+str(types)+"&key="+str(googlekey)

	while attempts < 3:
		try:
			r = requests.get(url).json()
			s = r['results']
			if not s: # This is kind of cheating, I'm assuming if google doesn't have an address for the GPS its over the ocean
				address.append("Nothing around, Sorry")
			else:	
				for key in s: 
					a = key['name']
					b = key['vicinity']
					try:
						c = key['opening_hours']['open_now']
 						addre={'name': a, 'vacinity':b,'open_now?':c}
					except:
						addre={'name': a, 'vacinity':b}
						pass 

					address.append(addre)
			break
		
		except: 
			attempts +=1
			print "error with placefromGPS"
			pass
	return address

addresses = placefromGPS()

for key in addresses:
	try:
		print "There is a " +str(key['name'])+ " at the address " +str(key['vacinity'])+ " and it is " +str(key['open_now?'])+ " that it is open now"
		break
	except:
		print "There is a " +str(key['name'])+ " at the address " +str(key['vacinity'])
		pass 