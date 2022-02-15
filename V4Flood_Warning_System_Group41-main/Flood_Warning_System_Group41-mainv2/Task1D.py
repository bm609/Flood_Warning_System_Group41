from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list()
    test = sorted(rivers_with_station(stations))
    print(len(test))    #prints length of test list
    print(test[:10])    #prints first 10 values in test
    statriver = stations_by_river(stations)
    print(sorted(statriver["River Aire"]))     #print sorted values corresponding to "River Aire" key
    print(sorted(statriver["River Cam"]))
    print(sorted(statriver["River Thames"]))
run()
