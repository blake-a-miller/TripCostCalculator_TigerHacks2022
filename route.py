import requests
import json
import datetime
import StateBounds as bounds
import ranges as gasRange

MapBoxToken = "pk.eyJ1IjoiamVybWIiLCJhIjoiY2xhMzdkaDQ4MDZxeTNvcnhhaHdxMzJ6NiJ9.F7i3IZFcmZM1UNP5pTPFBA"
MapBoxURL = "https://api.mapbox.com/directions/v5/"
MapBoxURL2 = "https://api.mapbox.com/geocoding/v5/mapbox.places/"

class Route:

    def __init__(self, start_location, end_location):
        self.states = []
        self.start_location = start_location
        self.end_location = end_location
        self.start_coord = self.getLatLong(start_location)
        self.end_coord = self.getLatLong(end_location)
        self.calcRoute(self.start_coord, self.end_coord)

    def getRouteDistance(self):
        return self.distance
    
    def getRouteTime(self):
        return self.distance

    def getLatLong(self, address):
        address = address.split(", ")
        address_format = []
        for x in address:
            x = x.strip()
            x = x.replace(" ", "%20")
            address_format.append(x)
        path = ""
        for item in address_format:
            path += f"{item},"
        path = path.rstrip(",")
        try:
            response = requests.get(f"{MapBoxURL2}{path}.json?access_token={MapBoxToken}&limit=1")
        except Exception as ex:
            # print("Exception: " + e)
            raise Exception
        data = response.json()
        coords = data.get("features")[0]["geometry"]["coordinates"]
        self.states.append(bounds.getState(coords))
        # print(bounds.getState(coords))
        return coords

    def calcRoute(self, start, end):
        # print(f"start={start}")
        # print(f"end={end}")
        response = requests.get(f"{MapBoxURL}mapbox/driving/{start[0]},{start[1]};{end[0]},{end[1]}?steps=true&access_token={MapBoxToken}")
        # waypoint_data = response.json().get("routes")[0].get("legs")[0].get("steps")[0].get("intersections")[0].get("location")
        data = response.json().get("routes")[0]
        waypoint_data = data.get("legs")[0].get("steps")
        
        list_of_waypoints = []
        for step in waypoint_data:
            intersection = step.get("intersections")
            list_of_waypoints.append(intersection[0].get("location"))
            list_of_waypoints.append(intersection[len(intersection)-1].get("location"))
            list_of_waypoints.append(intersection[int(len(intersection)/2)].get("location"))
        self.avgGasPrice(list_of_waypoints)
        self.distance = (float(data.get("distance")) / 1000) * 0.62137 # converts to miles
        self.duration = str(datetime.timedelta(seconds=(float(data.get("duration"))))) # time formatted

    def avgGasPrice(self, waypoints):
        for point in waypoints:
            state = bounds.getState(point)
            if state not in self.states:
                self.states.append(state)
        # print(self.states)      