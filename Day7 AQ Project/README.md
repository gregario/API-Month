Day 7 of the API Month. 

Bit of background on this one. I decided to do something a bit more abitious today. Since I now have the basic building blocks of data for getting and 
manipulating JSON API data I thought I would put it to the test for something more than one localised test. 
So today I'm going to build something chunkier. Using the work I've done all week from data manipulation, geocaching and the air quality API, I want to build an app that if you put in a post code in London it finds the nearest AQ monitor from the list and returns its air quality data. 

This is more challenging than it sounds, the basic work flow would be. 

Take input address and convert to GPS. 
Pull down list of all London Air Quality monitors and extract their locations. 
Do a diff between the two to find the closest distance from that new list.
Then from that monitor pull out its air quality monitor. 

What I can then use this to do is to give Air quality information as an extension to map or location searches. An interesting wrapper library for future work. I'm going to try some more complex error handling in this too, as I've been pretty lax with this up until now. 

One thing I've noticed from this work is I need to have a play with times and dates to do it neatly. Tomorrow I'm going to play with NTP servers and the date module in python. 
Its a slight divergence from the API calling but will be a useful function to plug into other functions in the future. 
