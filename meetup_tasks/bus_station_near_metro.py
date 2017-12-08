'''
Остановки у метро

Объединить наборы данных из предыдущих задач и посчитать, 
у какой станции метро больше всего остановок (в радиусе 0.5 км).
'''

import csv
import json
import re
from math import sin, cos, sqrt, atan2, radians
from bus_stop import count_key


def distance(coord1, coord2):
    # Haversine formula
    # R == approximate radius of earth in km
    R = 6373.0

    lon1 = radians(coord1[0])
    lat1 = radians(coord1[1])
    lon2 = radians(coord2[0])
    lat2 = radians(coord2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def is_near(coord, coord_list, dist=0.5):
    for c in coord_list:
        d = distance(c, coord)
        if d <= dist:
            return True
    return False
    
def get_bus_stops_coordinates(filename):
    bus_stops_coordinates = []
    with open(filename, "r") as f:
        bus_station_data = csv.reader(f, delimiter = ";")
        for line in bus_station_data:
            bus_stops_coordinates.append([float(line[2]), float(line[3])])
    return bus_stops_coordinates

def get_metro_coordinates(filename):
    metro_coordinates = {}
    with open(filename, "r") as f:
        metro_exit_data = json.load(f)
        for obj in metro_exit_data:
            exit_coord = obj["geoData"]["coordinates"]
            metro_name = obj["NameOfStation"]
            if metro_name not in metro_coordinates:
                metro_coordinates[metro_name] = []
            exit_coord_list = metro_coordinates[metro_name]
            exit_coord_list.append(exit_coord)
    return metro_coordinates 

def find_metro_with_max_stops(bus_stops_coordinates, metro_coordinates):
    max_stops = 0
    max_stops_metro_station = None
    bus_stops_by_metro = {}
    for metro_name in metro_coordinates:
        exit_coord_list = metro_coordinates[metro_name]
        for coord in bus_stops_coordinates:
            suitable = is_near(coord, exit_coord_list, dist=0.5)
            if suitable:
                stop_count = count_key(metro_name, bus_stops_by_metro)
                if stop_count > max_stops:
                    max_stops_metro_station = metro_name
                    max_stops = stop_count
    return max_stops_metro_station

max_stops_metro_station = find_metro_with_max_stops(
    get_bus_stops_coordinates("full_bus_data.csv"), 
    get_metro_coordinates("metro_rep.json")
)

print(max_stops_metro_station)
