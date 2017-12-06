# Остановки у метро

# Объединить наборы данных из предыдущих задач и посчитать, у какой станции метро больше всего остановок (в радиусе 0.5 км).

import csv
import json
import re
from math import sin, cos, sqrt, atan2, radians

bus_stops_by_metro = {}

def distance(coord1, coord2):
    # approximate radius of earth in km
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
        
    
bus_st_coordinates = []

with open("full_bus_data.csv", "r") as f:
    data_bus_station = csv.reader(f, delimiter = ";")    
    for line in data_bus_station:
        bus_st_coordinates.append([float(line[2]), float(line[3])])

metro_st_coordinates = {}
        
with open("metro_rep.json", "r") as f:
    data_metro_exit = json.load(f)
    for metro_exit in data_metro_exit:
        metro_coord = metro_exit["geoData"]["coordinates"]
        metro_name = metro_exit["NameOfStation"]
        if metro_name not in metro_st_coordinates:
            metro_st_coordinates[metro_name] = []
        metro_exit_coord_list = metro_st_coordinates[metro_name]
        metro_exit_coord_list.append(metro_coord)

result = None
max_stops = 0

for metro_name in metro_st_coordinates:
    metro_exit_coord_list = metro_st_coordinates[metro_name]
    for coord in bus_st_coordinates:
        suitable = is_near(coord, metro_exit_coord_list, dist=0.5)
        if suitable:
            if metro_name not in bus_stops_by_metro:
                bus_stops_by_metro[metro_name] = 0
            stop_count = bus_stops_by_metro[metro_name]
            stop_count += 1
            bus_stops_by_metro[metro_name] = stop_count
            
            if stop_count > max_stops:
                result = metro_name
                max_stops = stop_count
            

print(result)