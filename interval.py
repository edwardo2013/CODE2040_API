import json
import requests
import datetime
from mytoken import mytoken # Dont want to give away my token!


tok = mytoken()
data = json.loads(requests.post("http://challenge.code2040.org/api/time",data= json.dumps(tok)).content)
date = data['result']['datestamp'].encode('ascii')
res = date.replace('T'," ")
res = res.replace('Z',"")
interval = data['result']['interval']
print date, interval

# TODO UTC time zone aware
mytime = datetime.datetime.strptime(res, "%Y-%m-%d %H:%M:%S.%f")
mytime += datetime.timedelta(seconds=interval)
myresult = {'token':tok['token'],'datestamp':mytime.isoformat()}
response = requests.post("http://challenge.code2040.org/api/validatetime",data=json.dumps(myresult))
print response.content