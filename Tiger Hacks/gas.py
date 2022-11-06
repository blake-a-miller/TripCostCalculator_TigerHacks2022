import requests
import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 4ADfdP0bmIMZiHSGsUsNMU:1fmU8g2Q3VETlPx5jMBcLP"
    }

conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))