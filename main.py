import pandas as pd
import ast
import time

bus_stop = pd.read_csv('bus_stop.csv')
attraction = pd.read_csv('attraction.csv')
attraction_busStop = pd.read_csv('attraction&station.csv')
bus_stops_journey = pd.read_csv('line&station.csv')

station_to_attrction = pd.DataFrame(columns=['station', 'attraction', 'lines'])
i = 0
for first_station in bus_stop['stop_code'].unique():
    print(i)
    T = time.time()
    for atr in attraction_busStop['attraction'].unique():
        optional_stations = attraction_busStop.loc[attraction_busStop['attraction'] == atr, 'bus_stations'].iloc[0]
        optional_stations = ast.literal_eval(optional_stations)
        optinal_lines = list()
        for idx, row in bus_stops_journey.iterrows():
            bus = row['busId']
            bus_stations = row['stops']
            bus_stations = ast.literal_eval(bus_stations)
            if first_station not in bus_stations:
                continue
            for optional_s in optional_stations:
                if optional_s in bus_stations:
                    if bus_stations.index(first_station) < bus_stations.index(optional_s):
                        optinal_lines.append(bus)
                        break
        station_to_attrction.at[-1] = [first_station, atr, optinal_lines]
        station_to_attrction.index = station_to_attrction.index + 1
    print(time.time()-T)
    i += 1
