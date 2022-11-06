import re
import route
import prices
import ranges
import prompts
import car

def main():
    name = prompts.getName()
    addressing = True
    trip = None
    start = None
    end = None
    while(addressing):
        print("What is your current location?")
        start = f"{prompts.getAddress()}, {prompts.getCity()}, {prompts.getState()}"
        print("Where are you going?")
        end = f"{prompts.getAddress()}, {prompts.getCity()}, {prompts.getState()}"
        addressing=False
        try:
            trip = route.Route(start, end)
        except:
            print("Sorry! One of the locations you input was invalid. Please try again.\n")

    carIDing = True
    while(carIDing):
        try:
            make = prompts.getMake()
            model = prompts.getModel()
            year = prompts.getYear()

            mpg = car.getMPG(make, model, year)
            fuel_type = car.getFuelType(make, model, year)
            car_type = car.carType(make, model, year)

            gas_price = prices.getGasPrice(trip.states, fuel_type)
            total_gas_price = car.totalCost(mpg, trip.distance, gas_price)
            print(f"Excellent, {name}. You will be traveling to: {end} in your {year} {make} {model}.")
            print(f"It is {trip.distance} miles. Trip duration: {trip.duration}")
            print(f"The average cost of gas on the way to your destination is ${gas_price}.")
            print(f"It will cost ~${total_gas_price}.")
            ranges.getFillups(car_type, trip)
            carIDing = False
        except Exception as e:
            print(e)
            print("There was an issue processing your car. Please try again.\n")

    print("Thank you for using our service!")

main()



