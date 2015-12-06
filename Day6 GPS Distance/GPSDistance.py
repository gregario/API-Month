# -*- coding: utf-8 -*-T
# Program to check the linear distance between two sets of GPS coordinates. 
# Continuation of day 4 of API Month
# Greg Jackson 6th deb 2015
# Twitter @gr3gario or github gregario
# Day 6 of the Month of API

import googlemaps # install using pip install -U googlemaps 
import sys # Used to take in input parameters from command line.
from APIKEY import googlekey
import math # Added to do sqrt 

# Geocoding an address
geocode_result = gmaps.geocode(sys.argv[1]) # passes address given on command line to google maps geocoding api
gmaps = googlemaps.Client(key= googlekey) # Get key from your google developer portal. 
latlng = []
latlngTB = [51.5054564,-0.0753565]


for key in geocode_result: # the returned object is a list with nested JSON objects inside each list. So you need to iterate through the list and do operations on each object separately
	latlng.append(key['geometry']['bounds']['northeast']['lat']) # pulls out nested latitude figure from call
	latlng.append(key['geometry']['bounds']['northeast']['lng']) # pulls out nested longditude figure from call


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# Obsolete Method, simplier than other.
#distance = abs(latlngTB[0] - latlng[0]) + abs(latlng[1] - latlngTB[1]) 

distance = distance(latlng,latlngTB)
print "The distance to Tower Bridge is: " +str(distance)