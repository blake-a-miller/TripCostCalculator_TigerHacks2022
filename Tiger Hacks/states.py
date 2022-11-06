import requests
import http.client
import json

states = "AL,AK,AZ,AR,CA,CO,CT,DE,FL,GA,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VT,VA,WA,WV,WI,WY"
states = states.split(",")

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    "content-type": "application/json",
    "authorization": "apikey 4ADfdP0bmIMZiHSGsUsNMU:1fmU8g2Q3VETlPx5jMBcLP"
}

statesFile = open("GasPricesByState.txt", "w")
statesFile.write("{")

for state in states:
    conn.request("GET", f"/gasPrice/stateUsaPrice?state={state}", headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    state_info = data.get("result").get("state") #get info wanted from data here

    

    statesFile.write(f"\"{state}\":{state_info}")
    

statesFile.write("}")
statesFile.close()



