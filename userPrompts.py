print("Hello, welcome to the advanced trip planner! What is your name?")
username = input("")
print("")

print("Alright ," + username, "let's get started!") 
print("")

print("What is your destination? Enter city, state, zip. Example: 105 Jesse Hall Columbia, MO 65211")
destination = input("")

print("Enter the year your vehicle was made: ")
year = input("")

print("Enter the make of your vehicle: ")
make = input("")

print("Enter the model of your vehicle: ")
model = input("")

print("Excellent, " + username + ". You will be traveling to " + destination + " in your " + year + " " + make + " " + model + ".")