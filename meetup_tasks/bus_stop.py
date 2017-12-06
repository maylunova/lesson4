# Остановки

# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок.

import csv

with open ("bus_data.csv", "r") as f:
    reader = csv.reader(f, delimiter = ";")
    street_dict = {}
    result = None
    max_stops = 0
    for line in reader:
        street = line[0]
        if street not in street_dict:
            street_dict[street] = 0
        stop_count = street_dict[street]
        stop_count += 1
        street_dict[street] = stop_count

        if stop_count > max_stops:
            result = street
            max_stops = stop_count
            
    print(result)