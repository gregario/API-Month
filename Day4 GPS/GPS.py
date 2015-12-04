# -*- coding: utf-8 -*-
# Program to check how long it will take me to get to work
# Greg Jackson 4th deb 2015
# Twitter @gr3gario or github gregario
# Day four of the Month of API

import googlemaps # install using pip install -U googlemaps 
import sys # Used to take in input parameters from command line.

gmaps = googlemaps.Client(key='INSERT API KEY') # Get key from your google developer portal. 

# Geocoding an address
geocode_result = gmaps.geocode(sys.argv[1]) # passes address given on command line to google maps geocoding api
latlng = []

for key in geocode_result: # the returned object is a list with nested JSON objects inside each list. So you need to iterate through the list and do operations on each object separately
	latlng.append(key['geometry']['bounds']['northeast']['lat']) # pulls out nested latitude figure from call
	latlng.append(key['geometry']['bounds']['northeast']['lng']) # pulls out nested longditude figure from call

# easy peasy printing
print "Your latitude is: " +latlng[0]
print "Your londitude is: " +latlng[1]

