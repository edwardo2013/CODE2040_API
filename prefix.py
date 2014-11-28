import json
import requests
from mytoken import mytoken # Dont want to give away my token!


tok = mytoken()
data = json.loads(requests.post("http://challenge.code2040.org/api/prefix",data= json.dumps(tok)).content)
prefix = data['result']['prefix'].encode('ascii')
# The power of lambda!
Array = map(lambda x: x.encode('ascii'),data['result']['array'])
result = filter(lambda x: prefix not in x[0:len(x)], Array)
myresult = {'token':tok['token'],'array':result}
response = requests.post("http://challenge.code2040.org/api/validateprefix",data=json.dumps(myresult))
print response.content
