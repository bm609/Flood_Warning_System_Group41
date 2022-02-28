from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_level_over_threshold(stations, 0.8)
    for i in list:
        print(i[0].name, i[1])
run()