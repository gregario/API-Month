#coding: utf-8
# Day seven of the month of API
# Today finds your nearest Air Quality monitor and returns its data
# Greg Jackson @gr3gario on twitter and gregario on github

import requests
import json 
import sys  
import googlemaps
from APIKEY import googlekey
import math

## Workflow
#Pull down list of all London Air Quality monitors and extract their locations. 
#Do a diff between the two to find the closest distance from that new list.
#Then from that monitor pull out its air quality monitor. 

# This function takes in a command line post code (or address), performs a google maps call to check its GPS data and returns as a list
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

# This function calls the London Air Quality API and returns a list of all the sites with their GPS Coordinates 
def LAQNList():
	url = "http://api.erg.kcl.ac.uk/AirQuality/Information/MonitoringSites/GroupName=All/JSON" # Gives all units in London for AQ
	siteDetails=[]
	siteDetail={}
	attempts=0
	distance = 0.0

	while attempts < 3:
		try: 
			r = requests.get(url).json() # Make a request to the TFL API for data
			q = r['Sites']['Site'] # This extracts the list from the JSON object

			for key in q:
				# This is quite elegant. There are closed air quality units on the system which we want to ignore. So we check the dateclosed field. If its emply we include the unit. 
				dateclosed = key ['@DateClosed'] 
				if not dateclosed: 
					sitecode = key['@SiteCode']
					latitude = float(key['@Latitude'])
					longditude = float(key['@Longitude'])
					siteDetail={'sitecode': sitecode, 'latitude': latitude, 'longditude': longditude, 'distance':distance}
					siteDetails.append(siteDetail)
			break

		except:
			attempts += 1
			#print "Error getting Location data from LAQN API"

	return siteDetails

# This function takes input values and calculates distance for every point and calculates the closest site code
def distance():
    latlngin = addtoGPS()
    siteDetails=LAQNList()
    distance = []
    for key in siteDetails:
    	lat = float(key ['latitude'])
    	lng = float(key ['longditude'])
    	output = math.sqrt((latlngin[0] - lat)**2 + (latlngin[1] - lng)**2)
    	key['distance'] = output
    	distance.append(output)

    mindistance = min(distance)

    for key in siteDetails:
    	check = key['distance']
    	if check == mindistance: 
    		finalsite = key['sitecode']

    return finalsite

## I now have my closest Air Quality Monitor, need to call this and see what sensors it has
## back to the API documentation

def whatSensor():
	siteCode = distance()
	speciesCode = []
	attempts = 0 

	
	while attempts < 3:
		try: 
			url= "http://api.erg.kcl.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode=" +siteCode+ "/json"
			r = requests.get(url).json() # Make a request to the TFL API for data
			q = r['DailyAirQualityIndex']['LocalAuthority']['Site']['Species'] # This extracts the list from the JSON object
			for key in q:
				specie = key['@SpeciesCode']
				species={'SpeciesCode': specie}
				speciesCode.append(species)
			break

		except:
			attempts += 1
			print "error finding speciesCode of sensors"
	

	return speciesCode

# Finally once we have the sensors associated with the closest air quality sensor we can do a check of the last day and return an average of the readings
# I realise here it would be nice to check the current time and return it as a variable for input, will work on that on day 8
def sensorReadings():
	siteCode = distance()
	speciesCode = whatSensor()
	attempts = 0 
	averageOut  = []

	for key in speciesCode:
		speciesUrl = key['SpeciesCode']
		url = "http://api.erg.kcl.ac.uk/AirQuality/Data/SiteSpecies/SiteCode="+siteCode+"/SpeciesCode="+speciesUrl+"/StartDate=05-12-15/EndDate=06-12-15/Json" # Gives data in closest AQ monitor
		r = requests.get(url).json() # Make a request to the LAQN API for data

		rLoop = r['RawAQData']['Data']
		AQugm3 = [] 

		for key in rLoop:
			AQugm3temp = key['@Value'] 
			try: 
		 		AQugm3temp = float(AQugm3temp) 
		 		AQugm3.append(AQugm3temp) # Adds output to AQugm3 variable
		 	# Catches exceptions
		 	except:
		 		print 'error in parsing, oops'
		 		pass
		# Really simple averages. Sums all elements in the list and divides by the length of the list 
		average = sum(AQugm3) / float(len(AQugm3))
		average = round(average,2)
		average={'SpeciesCode': speciesUrl, 'average':average}
		averageOut.append(average)
	
	return averageOut

print sensorReadings()