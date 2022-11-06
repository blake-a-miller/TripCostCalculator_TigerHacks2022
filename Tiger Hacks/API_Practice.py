import requests
import xmltodict


 
fuelEconomy = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year=2012&make=Honda&model=Accord"
response = requests.get(fuelEconomy)
data = xmltodict.parse(response.content)

car = data.get("menuItems").get("menuItem")[0].get("text")
carID = data.get("menuItems").get("menuItem")[0].get("value")

print(car)
print(carID)

#print(data)







#response = requests.get(fuelEconomy)
#print(response.status_code)



#print(response.xml())
