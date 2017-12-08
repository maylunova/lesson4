'''
Остановки

Считать из csv-файла (с http://data.mos.ru/datasets/752) 
количество остановок, вывести улицу, на которой больше всего остановок.
'''

import csv

def count_key(key, dictionary):
    if key not in dictionary:
        dictionary[key] = 0
    cnt = dictionary[key]
    cnt += 1
    dictionary[key] = cnt
    return cnt
        
if __name__ == '__main__':
    max_stops_street = None
    with open ("bus_data.csv", "r") as f:
        reader = csv.reader(f, delimiter = ";")
        street_dict = {}
        max_stops = 0
        for line in reader:
            street = line[0]
            stop_count = count_key(street, street_dict)
            if stop_count > max_stops:
                max_stops_street = street
                max_stops = stop_count       
    print(max_stops_street)




        