# ==========================================================
# Author: Edwardo S. Rivera 
# Date: November 28,2014
# email: edwardo.rivera@upr.edu
# Description: This program adds a time interval (in seconds)
# to a given date usins the datetime library of Python. 
# Part of the CODE 2040 API Challenge. Stage 2.
# ==========================================================
from json import loads,dumps
from requests import post
from mytoken import mytoken
from datetime import datetime,timedelta

# Again, my token.
tok = mytoken()
# As in Stage 3, fetch the data fron the server
data = loads(post("http://challenge.code2040.org/api/time",data= dumps(tok)).content)
# Sanitize data (to python string)
date = data['result']['datestamp'].encode('ascii')
# replace the separator and UTC code ("Z")
res = date.replace('T'," ")
# Important Note: Because the time is given in UTC format, and we are not using
# our local time, the only thing left to do is to add the dates, that is why I can remove the Z code
res = res.replace('Z',"")
# Get the interval number (in seconds)
interval = data['result']['interval']
print " The given date is", date, " and the interval is:",interval
# To add the interval to the given time, format it as a datetime object
# Use strptime to format the datatime object that we want to format. res is a string.
# See: https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
# No need to do slice operations or other stuff. 
mytime = datetime.strptime(res, "%Y-%m-%d %H:%M:%S.%f")
# This is what we want to do: sum a datetime object with time delta.
# Time delta does the work, no conversions needed!
mytime += timedelta(seconds=interval)
print "The resulting date is",mytime.isoformat()
# Pack the result in iso 8601 format and send it to the server
myresult = {'token':tok['token'],'datestamp':mytime.isoformat()}
response = post("http://challenge.code2040.org/api/validatetime",data=dumps(myresult))
# Print the server response
print loads(response.content).get('result')