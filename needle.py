# ==========================================================
# Author: Edwardo S. Rivera 
# Date: November 28,2014
# email: edwardo.rivera@upr.edu
# Description: This program reverses a string using the API
# of the CODE 2040 API Challenge. Stage 2.
# ==========================================================
from json import loads,dumps
from requests import post
from mytoken import mytoken

# Use this for other language like C++ :)
def findNed(ned,array):
	""" Returns the index where ned is inside the array"""
	for i in range(0,len(array)):
		if array[i] == ned:
			return i
	return -1 # Index not found: give a negative number

if __name__ == '__main__':
	# My token
	tok = mytoken()
	# Do the post to the corresponding link (see reverse.py for more details)
	response = post("http://challenge.code2040.org/api/haystack",data= dumps(tok))
	# The content is in JSON format, so unpack and get the Python dictionary
	info = loads(response.content)
	# Get the needle and print it. Remember to convert unicode to ascii
	ned = info['result']['needle'].encode('ascii')
	print "Neddle is: ", ned
	# Use map: pass a lambda function to create a list of python strings (not unicode). 
	l = map(lambda x: x.encode('ascii'),info['result']['haystack'])
	print "List is: ", l 
	#Find the index where ned is (the challenge)
	ned_index = l.index(ned)
	print "index is: ", ned_index
	# Pack result. Send the post back to the server.
	myresult = {'token':tok['token'],'needle':ned_index}
	response2 = post("http://challenge.code2040.org/api/validateneedle",data= dumps(myresult))
	# Print the server response
	print loads(response2.content).get('result')