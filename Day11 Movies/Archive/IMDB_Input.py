import requests
import sys
import time

my_list = sys.argv
print my_list
imdb_list =[]

for key in my_list[1:]:
	new_str = key.replace(" ","+")
	url = 'http://www.omdbapi.com/?t=' +new_str+ '&y=&plot=short&r=json'
	r = requests.get(url).json() # Make a request to the TFL API for data
	s = r['imdbRating']
	imdb_list.append(float(s))
	print 'The show {0} has the imdb score {1}'.format(key,s)

output = sum(imdb_list)
print "The total  imdb score is %f" %output