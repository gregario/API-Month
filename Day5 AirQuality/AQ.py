import requests
import json 


url = "http://api.erg.kcl.ac.uk/AirQuality/Data/SiteSpecies/SiteCode=IS2/SpeciesCode=NO2/StartDate=04-12-15/EndDate=05-12-15/Json" # Gives data in closest AQ monitor
r = requests.get(url).json() # Make a request to the LAQN API for data

rLoop = r['RawAQData']['Data'] # You got to define this here as you can't nest it below. the for loop below only works for the list embedded in the JSON object
AQugm3 = [] # A list to store the readins


for key in rLoop:
	AQugm3temp = key['@Value'] # This loops through each data packet in the list and pulls out our relevant datapoint
	try: # A try catch is included here as there are blank datapoints returned from the LAQN API that would mess this up occasionally if there wasn't a catch in place
		AQugm3temp = float(AQugm3temp) # Converts from a string to a float so we can perform operations on it
		AQugm3.append(AQugm3temp) # Adds output to AQugm3 variable
	# Catches exceptions
	except:
		print 'error in parsing, oops'
		pass

# Really simple averages. Sums all elements in the list and divides by the length of the list 
average = sum(AQugm3) / float(len(AQugm3))
average = round(average,2)
# This is an EU defined goal for NO2 in the city. I figure if our daily average is below this we're doing well. Its more to give context to the number.
goal = 40.0 

# Simple check to give context to the number. 
if average < goal:
	print "Hurray! The air quality today is less than the yearly average target of 40 ug/m3 NO2 target in the UK and reads " +str(average)+ " ug/m3"
elif average > goal: 
	print "Unfortunately the air quality today is more than the yearly average target of 40 ug/m3 NO2 in the UK and reads " + str(average)+ " ug/m3"
