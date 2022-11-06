import xmltodict
import requests

FuelEconomyURL = "https://www.fueleconomy.gov"






"""path = "/ws/rest/ympg/shared/vehicles?make=Honda&model=Fit"

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
    print("Fuel Type: "+fuelType)
"""

def getMPG(make, model, year):
    
    path = "/ws/rest/ympg/shared/vehicles?make=" + make + "&model=" + model

    MPG = "0"
    
    response = requests.get(FuelEconomyURL+path)
    
    data = xmltodict.parse(response.content)

    for x in data.get("vehicles").get("vehicle"):
        if x.get("year")==year:
            MPG = x.get("comb08")
            break
        else:
            continue
    
    if(MPG=="0"):
        return "Car not supported"
    else:
        return MPG

def getFuelType(make, model, year):
    
    path = "/ws/rest/ympg/shared/vehicles?make=" + make + "&model=" + model

    fuelType = "Regular"
    
    response = requests.get(FuelEconomyURL+path)
    
    data = xmltodict.parse(response.content)

    for x in data.get("vehicles").get("vehicle"):
        if x.get("year")==year:
            fuelType = x.get("fuelType")
            break
        else:
            continue
    

    return fuelType

def carType(make, model, year):
    path = "/ws/rest/ympg/shared/vehicles?make=" + make + "&model=" + model

    VClass = "none"
    
    response = requests.get(FuelEconomyURL+path)
    
    data = xmltodict.parse(response.content)

    for x in data.get("vehicles").get("vehicle"):
        if x.get("year")==year:
            VClass = x.get("VClass")
            break
        else:
            continue
    

    if(VClass=="none"):
        return "Range not supported"
    else:
        return VClass


def totalCost(mpg, distance, gasPrice):
    total = (distance * gasPrice)/mpg
    return total
