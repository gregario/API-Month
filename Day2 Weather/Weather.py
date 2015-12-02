# -*- coding: utf-8 -*-
# Program to check how long it will take me to get to work
# Greg Jackson 1st dev 2015
# Twitter @gr3gario or github gregario
# Day one of the Month of API

import requests
import json 

country= 'uk'
location = 'London'
url = "http://api.wunderground.com/api/2bd1140d98066169/conditions/q/"+str(country)+"/"+str(location)+".json"

r = requests.get(url).json()
print("The current wind speed (mph) is: "+ str(r['current_observation']['wind_mph']))
print("The current temperature (C) is: " +str(r['current_observation']['temp_c']))
print("Sure what's the weather like? : "+ str(r['current_observation']['icon']))
print("The current relative RH is: "+str(r['current_observation']['relative_humidity']))
print("Will it rain soon? : "+str(r['current_observation']['precip_1hr_metric']))

# So I have a good indication of the weather from a current loation. 
# I introduced two super simple things here. 
# One is string concatonation in python. This lets us declare a location by variable instead of in line. 
# this can be better than the payload option as it gives you more flexibility. 

## Finally I thought I could declare from the command line the location to search. 
## I've always wondered how this could be done so now I know! 