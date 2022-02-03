
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    #print(stations[1].name)
    list = inconsistent_typical_range_stations(stations)
    list.sort(key = lambda x: x.name)
    print(list)
run()