import requests
import xmltodict
import json
MapBoxToken = "pk.eyJ1IjoiamVybWIiLCJhIjoiY2xhMzdkaDQ4MDZxeTNvcnhhaHdxMzJ6NiJ9.F7i3IZFcmZM1UNP5pTPFBA"
MapBoxURL = "https://api.mapbox.com/directions/v5/"
# https://api.mapbox.com/directions/v5/{profile}/{coordinates}
FuelEconomyURL = "https://www.fueleconomy.gov/ws/rest/"

def main():
    response = requests.get(MapBoxURL + "mapbox/driving/-92.3215827,38.9112572;-92.332617,38.9459675?access_token=" + MapBoxToken)
    print(response)
    # route = json.load(response.content)
    print(response.json())
    # car = car(2012, "Honda", "Accord")
    # mpg = getMPG(carID)
    # print(mpg)

def getxml(path):
    try:
        response = requests.get(FuelEconomyURL + path)
        data = xmltodict.parse(response.content)
        print(data)
        return data
    except Exception as ex:
        print("Exception: " + ex)

def car(year, make, model):
    path = f"vehicle/menu/options?year={year}&make={make}&model={model}"
    return getxml(path).get("menuItems").get("menuItem")[0].get("value")
    # print(car)
    # getMPG(car)
#     # if year==None or make==None or model==None:
#     #     raise Exception("Please fill out all parameters")
#     # else:
#     #     path = f"year={year}&make={make}&model={model}"
#     #     getxml(path)

def getMPG(car):
    path = f"ympg/shared/ympgVehicle/{car}"
    return getxml(path).get("yourMpgVehicle").get("avgMpg")

if __name__ == "__main__":
    main()