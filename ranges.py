import math
import route

def getFillups(carType, route):
    gasRange = gasVehicleRange[carType]

    if route.distance > gasRange:
        fills = math.floor(route.distance / gasRange)
        print(f"You'll need to fill up at least {fills} times.")
    else:
        print("You might not need to fill up at all!")

gasVehicleRange = {
  "Compact Cars": 450,
  "Midsize Cars": 440,
  "Large Cars": 430,
  "Midsize Station Wagons": 430,
  "Midsize-Large Station Wagons": 420,
  "Minicompact Cars": 410,
  "Minivan - 2WD": 435,
  "Minivan - 4WD": 415,
  "Small Pickup Trucks": 430,
  "Small Pickup Trucks 2WD": 450,
  "Small Pickup Trucks 4WD": 450,
  "Small Sport Utility Vehicle 2WD": 400,
  "Small Sport Utility Vehicle 4WD": 390,
  "Small Station Wagons": 420,
  "Special Purpose Vehicle": 400,
  "Special Purpose Vehicle 2WD": 400,
  "Special Purpose Vehicle 4WD": 380,
  "Special Purpose Vehicles": 400,
  "Special Purpose Vehicles/2wd": 400,
  "Special Purpose Vehicles/4wd": 380,
  "Sport Utility Vehicle - 2WD": 440,
  "Sport Utility Vehicle - 4WD": 420,
  "Standard Pickup Trucks": 430,
  "Standard Pickup Trucks 2WD": 430,
  "Standard Pickup Trucks 4WD": 380,
  "Standard Pickup Trucks/2wd": 430,
  "Standard Sport Utility Vehicle 2WD": 440,
  "Standard Sport Utility Vehicle 4WD": 410,
  "Subcompact Cars": 420,
  "Two Seaters": 450,
  "Vans": 440,
  "Vans Passenger": 430,
  "Vans, Cargo Type": 390,
  "Vans, Passenger Type": 430,
}