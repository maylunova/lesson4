'''
Метро

В этом задании требуется определить, на каких станциях московского метро сейчас 
идёт ремонт эскалаторов и вывести на экран их названия.
'''

import json

full_data = json.load(open('metro_rep.json', 'r'))
data = set()
for line in full_data:
    repair_of_escalators = line["RepairOfEscalators"]
    if len(repair_of_escalators) > 0:
        metro_station_name = line["NameOfStation"]
        data.add(metro_station_name)
        
for line in data:    
    print(line)