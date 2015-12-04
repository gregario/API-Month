# -*- coding: utf-8 -*-
# Program to check how long it will take me to get to work
# Greg Jackson 1st dev 2015
# Twitter @gr3gario or github gregario
# Day one of the Month of API

import requests
import json 
import sys # needed to pass arguments from command line 
import datetime
import time

url = "https://api.tfl.gov.uk/StopPoint/910grctryrd/arrivals" # the stop number is returned from the TFL website from a manual search. This calls the data
r = requests.get(url).json() # Make a request to the TFL API for data
time = [] # List for my future train arrivals
for key in r: # the returned object is a list with nested JSON objects inside each list. So you need to iterate through the list and do operations on each object separately
	if key['destinationName'] == ("Cheshunt Rail Station") or ("Enfield Town Rail Station"): # This filters out trains to different destinations. I can take either of these trains
		time.append(key['expectedArrival'])  # Adds expected arrival time from each train data structure to the time list

time_sorted = sorted(time) # sorts the time list so we get the train due to arrive first
time_train = time_sorted.pop(0) # pops out the first train to arrive and stores
#print time_train

# this translates the list to a usable 
time_train_temp = time_train.split('T',1)[-1]
time_train_parsed = time_train_temp.split('.',1)[0]
#print time_train_parsed


i = str(datetime.datetime.now())
j = i.split(' ',1)[-1]
k = j.split('.',1)[0]
#print  k

timeA = datetime.datetime.strptime(time_train_parsed, '%H:%M:%S')  
#print timeA
timeB = datetime.datetime.strptime(k, '%H:%M:%S') 
#print timeB

time_delta = timeA-timeB
print ("The next train to work will arrive in " +str(time_delta))

 
