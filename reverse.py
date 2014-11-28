import json
import requests
from mytoken import mytoken # Dont want to give away my token!

def reverse(mystr):
	L = []
	L.extend(mystr)
	size = len(L)
	for i in range(0,size/2):
		tmp = L[i]
		L[i]=L[size-i-1]
		L[size-i-1] = tmp
	return "".join(L)

tok = mytoken()
response = requests.post("http://challenge.code2040.org/api/getstring",data= json.dumps(tok))
string = json.loads(response.content).get('result').encode('ascii')
print string
# same as
#res = json.loads(response.content)
#res = res['result']
#res = res.encode('ascii')
result = reverse(string)
myresult = {'token':tok['token'],'string':result}
response2 = requests.post("http://challenge.code2040.org/api/validatestring",data= json.dumps(myresult))
print json.loads(response2.content).get('result')

