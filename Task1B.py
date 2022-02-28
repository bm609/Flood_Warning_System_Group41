from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""
    stations = build_station_list() # list of stations
    cam = (52.2053, 0.1218) # Cambridge city centre coordinate
    list = stations_by_distance(stations, cam)
    print(list[:10])
    print(list[-10:])
run()