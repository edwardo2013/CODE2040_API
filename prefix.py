# ==========================================================
# Author: Edwardo S. Rivera 
# Date: November 28,2014
# email: edwardo.rivera@upr.edu
# Description: This program finds where a prefix string is not
# part of the string (at the beggining), fo a series of 
# strings in a given array. Part of the CODE 2040 
# API Challenge. Stage 3.
# ==========================================================
from json import loads,dumps
from requests import post
from mytoken import mytoken

# My token
tok = mytoken()
# Lets do this in a fancy way: Use the post to fetch the data, and find the content of the data. 
# Then, use the loads function of the json library to decode to a python dictionary
data = loads(post("http://challenge.code2040.org/api/prefix",data= dumps(tok)).content)
# Get the prefix
prefix = data['result']['prefix'].encode('ascii')
# The power of lambda! Convert each array element from unicode to string, then find hte solution
# using filter, which is a lambda function creating a list of strings that do no have the prefix string 
Array = map(lambda x: x.encode('ascii'),data['result']['array'])
result = filter(lambda x: prefix not in x[0:len(prefix)], Array)
# print information
print "The prefix is: ", prefix
print "The Array is:", Array
print "The result list is ", result
# Unpack and send the result
myresult = {'token':tok['token'],'array':result}
response = post("http://challenge.code2040.org/api/validateprefix",data=dumps(myresult))
# Print the server response
print loads(response.content).get('result')
