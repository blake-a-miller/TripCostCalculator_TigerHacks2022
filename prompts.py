def getName():
    print("Hello, welcome to the advanced trip planner! What is your name?")
    username = input("")
    print("")

    print("Alright " + username,  ", let's get started!") 
    print("")
    return username

def getAddress():
    print("Enter the street address. Example: 325 Washington Street (hit ENTER to skip)")
    StreetAddress = input("")
    print("")
    return StreetAddress

def getCity():
    print("Enter City: ")
    City = input("")
    print("")
    return City

def getState():
    print("Enter State: ")
    State = input("")
    print("")
    return State

def getZipCode():
    prompt = True
    year = None
    while(prompt):
        print("Enter Zip Code: ")
        try:
            ZipCode = int(input(""))
            prompt = False
        except:
            print("Invalid Zipcode! Try again.")
            prompt=True
        finally:
            print("")
    return ZipCode

def getYear():
    prompt = True
    year = None
    while(prompt):
        print("Enter the year your vehicle was made: ")
        try:
            year = int(input(""))
            prompt=False
        except:
            print("Invalid year! Try again.")
            prompt=True
        finally:
            print("")
    return str(year)

def getMake():
    print("Enter the make of your vehicle: ")
    make = input("")
    print("")
    return make

def getModel():
    print("Enter the model of your vehicle: ")
    model = input("")
    print("")
    return model