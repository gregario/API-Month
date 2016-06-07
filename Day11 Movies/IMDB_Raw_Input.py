# Written by Greg Jackson for API month Day 11 07/06/16
# Game created to take different movie and TV shows and calculate their total IMDB score. 
# gr3gario on twitter and gregario on github
# Should probably include error checking if someone spells a movie incorrectly 

import requests
import sys
import time

imdb_list  =[] # Holds all the movie and TV inputs 
imdb_float =[] #
print "------------------------------------"
print "Add as many shows as you would like"
print "type f to finish"
print "------------------------------------"
timing = True

while timing:
	x = (raw_input('Add a show '))
	if str(x) is "f":
		timing = False
	else:
		imdb_list.append(x)

for key in imdb_list:
	new_str = key.replace(" ","+")
	url = 'http://www.omdbapi.com/?t=' +new_str+ '&y=&plot=short&r=json'
	r = requests.get(url).json() # Make a request to the TFL API for data
	s = r['imdbRating']
	imdb_float.append(float(s))
	print s
	print 'The show {0} has the imdb score {1}'.format(key,s)

output = sum(imdb_float)
print "The total  imdb score is %f" %output