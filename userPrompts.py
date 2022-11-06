print("Hello, welcome to the advanced trip planner! What is your name?")
username = input("")
print("")

print("Alright " + username,  ", let's get started!") 
print("")

print("What is your current location?")
print("Enter the street address. Example: 325 Washington Street")
currentStreetAddress = input("")
print("")

print("Enter City: ")
currentCity = input("")
print("")

print("Enter State: ")
currentState = input("")
print("")

print("Enter Zip Code: ")
currentZipCode = int(input(""))
print("")


print("What is your destination? Enter the street address.")
print("Example: 325 Washington Street")
streetAddress = input("")
print("")

print("Enter City: ")
city = input("")
print("")

print("Enter State: ")
state = input("")
print("")

print("Enter Zip Code: ")
zipCode = int(input(""))
print("")

print("Enter the year your vehicle was made: ")
year = int(input(""))
print("")

print("Enter the make of your vehicle: ")
make = input("")
print("")

print("Enter the model of your vehicle: ")
model = input("")
print("")

print("Excellent, {}. You will be traveling to: {}, {}, {} {}in your {} {} {}.".format(username, streetAddress, city, state, zipCode, year, make, model))