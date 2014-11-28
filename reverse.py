# ==========================================================
# Author: Edwardo S. Rivera 
# Date: November 27,2014
# email: edwardo.rivera@upr.edu
# Description: This program reverses a string. Part of the
# CODE 2040 API Challenge. Stage 1.
# ==========================================================
from json import loads,dumps
from requests import post
from mytoken import mytoken

# My reverse function 
# Note: Because Python string are inmutable, L.extend() time complexity is T(n) = n
# where n is the number of characters of the string. In C++ (can be done inplace): 
# Time complexity of algorithm = n/2 See the doc inside of the function. Is easy to see 
# that to swap the elements one has to go only to the middle of the string. 
def reverse(mystr):
	""" Reverse function. parameter: a string, output: the reversed string.
	    It swaps the first element not swaped with the last one not swaped
	    until all elements are done."""
	L = []
	L.extend(mystr)
	size = len(L)
	for i in range(0,size/2):
		# swap:
		tmp = L[i]
		L[i]=L[size-i-1]
		L[size-i-1] = tmp
	return "".join(L)

if __name__ == '__main__':

	# This is my token, see mytoken.py
	tok = mytoken()

	# Using the requests library of python, use a http post. Also, the dumps
	# function from the json library converts the token to a json object 
	response = post("http://challenge.code2040.org/api/getstring",data= dumps(tok))

	# Unpack: response.content has the json object, loads make the 
	# a Python dictionary and encode converts the unicode to a python string
	string = loads(response.content).get('result').encode('ascii')

	# Lets print the string
	print "The given string: ", string

	# The challege here! see the reverse function
	result = reverse(string)
	print "The reversed string: ",result

	# Build the structure of the JSON
	myresult = {'token':tok['token'],'string':result}

	# Now, do the post to the corresponding link
	response2 = post("http://challenge.code2040.org/api/validatestring",data= dumps(myresult))

	# print the response to see if we passed the test
	print loads(response2.content).get('result')