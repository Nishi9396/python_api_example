import http.client

conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "50f5ee0134mshc77266b576aad12p121f1ajsna0665bb13c6d",
    'x-rapidapi-host': "open-weather13.p.rapidapi.com"
}

conn.request("GET", "/city?city=new%20york&lang=EN", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import requests
import json

url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"new york","lang":"EN"}

headers = {
	"x-rapidapi-key": "50f5ee0134mshc77266b576aad12p121f1ajsna0665bb13c6d",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(json.dumps(response.json(),indent=4, sort_keys=True))
