import xmltodict
import requests

FuelEconomyURL = "https://www.fueleconomy.gov"
path = "/ws/rest/ympg/shared/vehicles?make=Honda&model=Fit"

tankSize = "0"
combinedMPG = "0"
fuelType = "regular"
year = "2020"

response = requests.get(FuelEconomyURL+path)
print(response)
data = xmltodict.parse(response.content)

#combinedMPG = data.get("vehicles").get("vehicle")[1].get("comb08U")

for x in data.get("vehicles").get("vehicle"):
    if x.get("year")==year:
        combinedMPG = x.get("comb08")
        fuelType = x.get("fuelType")
        break
    else:
        continue

if(combinedMPG == "0"):
    print("Car not supported")
else:
    print("MPG: "+combinedMPG)