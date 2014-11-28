import json
import requests
from mytoken import mytoken # Dont want to give away my token!

# Use this for other language :)
def findNed(ned,array):
	for i in range(0,len(array)):
		if array[i] == ned:
			return i
	return None

tok = mytoken()
response = requests.post("http://challenge.code2040.org/api/haystack",data= json.dumps(tok))
info = json.loads(response.content)
ned = info['result']['needle'].encode('ascii')
l = map(lambda x: x.encode('ascii'),info['result']['haystack']).index(ned) # Boom
myresult = {'token':tok['token'],'needle':l}
response2 = requests.post("http://challenge.code2040.org/api/validateneedle",data= json.dumps(myresult))
print response2.content