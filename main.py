import pandas as pd
import ast
import time

# bus_stops_in_each_journey = pd.read_csv('data/bus_stops_in_each_journey.csv')
# bus_lines_route = pd.read_csv('bus_lines_route.csv')
# a=1
# attraction = pd.read_csv('attraction.csv')
# attraction_busStop = pd.read_csv('attraction&station.csv')
# bus_stops_journey = pd.read_csv('line&station.csv')

# line_and_optional_stations_df = pd.DataFrame(columns=['lineId','stations'])
# line_and_optional_stations_dict = dict()
#
# for idx,row in bus_stop.iterrows():
#     optional_lines = row['routes_served'].split(', ')
#     for line in optional_lines:
#         if line not in line_and_optional_stations_dict:
#             line_and_optional_stations_dict[line] = [row['stop_code']]
#         else:
#             line_and_optional_stations_dict[line].append(row['stop_code'])
# for key,value in line_and_optional_stations_dict.items():
#     line_and_optional_stations_df.at[-1] = [key,value]
#     line_and_optional_stations_df.index = line_and_optional_stations_df.index + 1
#
# line_and_optional_stations_df.to_csv('line_and_optional_stations.csv',index=False)


# station_to_attrction = pd.DataFrame(columns=['station', 'attraction', 'lines'])
# i = 0
# for first_station in bus_stop['stop_code'].unique():
#     print(i)
#     T = time.time()
#     for atr in attraction_busStop['attraction'].unique():
#         optional_stations = attraction_busStop.loc[attraction_busStop['attraction'] == atr, 'bus_stations'].iloc[0]
#         optional_stations = ast.literal_eval(optional_stations)
#         optinal_lines = list()
#         for idx, row in bus_stops_journey.iterrows():
#             bus = row['busId']
#             bus_stations = row['stops']
#             bus_stations = ast.literal_eval(bus_stations)
#             if first_station not in bus_stations:
#                 continue
#             for optional_s in optional_stations:
#                 if optional_s in bus_stations:
#                     if bus_stations.index(first_station) < bus_stations.index(optional_s):
#                         optinal_lines.append(bus)
#                         break
#         station_to_attrction.at[-1] = [first_station, atr, optinal_lines]
#         station_to_attrction.index = station_to_attrction.index + 1
#     print(time.time()-T)
#     i += 1
