#coding: utf-8
# Day Eight of the month of API
# Today Looks at the internation space station
# Greg Jackson @gr3gario on twitter and gregario on github
# Thanks to everyone over at open-notify for providing such a cool API to play with

import requests
import json 
import sys  
import googlemaps
from APIKEY import googlekey
import time

def addtoGPS():
	attempts = 0
	latlng = []
	
	while attempts < 3:
		try:
			gmaps = googlemaps.Client(key=googlekey) # Get key from your google developer portal. 
			# Geocoding an address
			geocode_result = gmaps.geocode(sys.argv[1]) # passes address given on command line to google maps geocoding api
			
			for key in geocode_result: # the returned object is a list with nested JSON objects inside each list. So you need to iterate through the list and do operations on each object separately
				latlng.append(float(key['geometry']['bounds']['northeast']['lat'])) # pulls out nested latitude figure from call
				latlng.append(float(key['geometry']['bounds']['northeast']['lng'])) # pulls out nested longditude figure from call
			break
		
		except:
			attempts += 1
			print "Error getting data from Google maps API"	
	
	return latlng


def issPass():
	latlng=addtoGPS()
	url = "http://api.open-notify.org/iss-pass.json?lat="+str(latlng[0])+"&lon=" +str(latlng[1])
	attempts = 0
	print "The ISS will pass over the inputted position on the following dates: "
	while attempts < 3:
		try: 
			r = requests.get(url).json() # Make a request to the ISS API for data
			s = r['response']
			for key in s:
				duration = key['duration']
				risetime = key['risetime']
				risetime =time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(risetime))
				print " " +str(risetime)+ " for " +str(duration)+ " seconds"
			break
		except:
			print "error in parsing space"
			attempts +=1
			pass


def onBoard():
	url = "http://api.open-notify.org/astros.json"
	attempts = 0 
	astro = []

	while attempts < 3:
		try:
			r = requests.get(url).json()
			#
			s = r['people']
			for key in s: 
				astro.append(key['name'])
			
			# you could have also gotten this by doing len(astro)
			print "There are " +str(r['number'])+ " people on board, they are:"
			# you could have done this in the loop that saves the astronauts names but I wanted to iterate on the list too (it is less efficient)
			
			for key in astro:
				print key
	
			break
		except: 
			attempts +=1
			print "error with astro"
			pass

# It looks very straightfoward so I just decided to code this one without the googlemaps module
def GPStoadd(p0):
	
	url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(p0[0])+","+str(p0[1])+"&key="+str(googlekey)
	attempts = 0 
	address = []
	rbad = "{u'status': u'ZERO_RESULTS', u'results': []}"

	while attempts < 3:
		try:
			r = requests.get(url).json()
			s = r['results']
			if not s: # This is kind of cheating, I'm assuming if google doesn't have an address for the GPS its over the ocean
				address.append("the Ocean")
			else:	
				for key in s: 
					address.append(key['formatted_address'])		
			
			break
		
		except: 
			attempts +=1
			print "error with GPStoADD"
			pass
	return address[0]

#Passing in variables to return what I need, makes it more object oriented than I had in the first project where I was calling a function every time I needed the variable
def currentLoc():
	url = "http://api.open-notify.org/iss-now.json"
	attempts = 0
	latlng= []

	while attempts <3:
		try:
			r = requests.get(url).json()
			latlng.append(r['iss_position']['latitude'])
			latlng.append(r['iss_position']['longitude'])
			break
		except:
			attempts +=1
			print "error with ISS Loc"
			pass

	return GPStoadd(latlng)

print " " # There's probably a more elegant way of doing this but meh
print "========================================================================" 
print "The international space station is currently over " +str(currentLoc()) 
print " "
onBoard()
print " "
issPass()
print "========================================================================"
print " "