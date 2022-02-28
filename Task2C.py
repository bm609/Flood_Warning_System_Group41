from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    rel = stations_highest_rel_level(stations, 10)
    for i in range(0,len(rel)):
        print(rel[i].name, rel[i].relative_water_level())
run()