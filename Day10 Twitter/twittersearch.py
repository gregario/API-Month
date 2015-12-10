#coding: utf-8
# Day 10 of the month of API
# Today finds #sad and #happy online to see how the internet is feeling 
# Greg Jackson @gr3gario on twitter and gregario on github
# Code credit goes to ideoforms on github, I just added the happy vs sad bit

from twitter import *

# load our API credentials 
config = {}
execfile("config.py", config)

# create twitter API object
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

# Twitter API docs: https://dev.twitter.com/docs/api/1/get/search
query = twitter.search.tweets(q = "oasis")
query2 = twitter.search.tweets(q= "blur")

output1 = []
output2 = []
#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for key in query["statuses"]:
	output1.append(key["user"]["screen_name"])
	
for key in query2['statuses']:
	output2.append(key["user"]["screen_name"])

happyLength = len(output1)
sadLength = len(output2)

print output1
print output2
print "There are " +str(happyLength)+ " oasis people and " +str(sadLength)+ " blur people on the internet"
