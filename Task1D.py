from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    test = rivers_with_station(stations)
    print(test)
run()
