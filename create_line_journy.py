import pandas as pd
import math
from geopy import distance
import shapefile
import time

bus_stop = pd.read_csv('data/bus_stop.csv')
line_and_optional_stations = pd.read_csv('line_and_optional_stations.csv')
shape = shapefile.Reader("data/NTA_Public_Transport/NTA_Public_Transport.shp")
shape_dict = {r.record.route_name: r.shape for r in shape.shapeRecords()}  # {lineid : Shape}
bus_lines_route = dict()
bus_lines_route_df = pd.DataFrame(columns=['lineId', 'stations'])
print(len(shape_dict))
i_line = 1
for bus_line in shape_dict.keys():
    T = time.time()
    print(i_line)
    stops_route = list()
    parts = shape_dict[bus_line].parts
    points = shape_dict[bus_line].points
    geom = []
    for i in range(len(parts)):
        xy = []
        # pt = None
        if i < len(parts) - 1:
            pt = points[parts[i]:parts[i + 1]]
        else:
            pt = points[parts[i]:]
        for x, y in pt:
            xy.append([y, x])
        geom.append(xy)
    geom_flat = flat_list = [item for sublist in geom for item in sublist]
    print('geo len',len(geom_flat))
    for p_idx, p in enumerate(geom_flat):
        if p_idx % 3 == 0 and p_idx != 0:
            continue
        closest_to_p, min_dist_to_p = None, math.inf
        optinal_s = line_and_optional_stations[line_and_optional_stations['lineId'] == bus_line]['stations'].values[0].strip('[').strip(']').split(', ')
        for s in optinal_s:
            s = int(s)
            if s in stops_route:
                continue
            s_loc = (
            bus_stop[bus_stop['stop_code'] == s]['Y'].values[0], bus_stop[bus_stop['stop_code'] == s]['X'].values[0])
            dist = distance.distance(s_loc, p).m
            if dist < min_dist_to_p:
                closest_to_p = s
                min_dist_to_p = dist
        if min_dist_to_p < 15:
            stops_route.append(closest_to_p)
    bus_lines_route[bus_line] = stops_route
    bus_lines_route_df.at[-1] = [bus_line, stops_route]
    bus_lines_route_df.index = bus_lines_route_df.index + 1
    print(f'time for {i_line} is: {time.time() - T}')
    i_line += 1

bus_lines_route_df.to_csv('bus_lines_route.csv')
