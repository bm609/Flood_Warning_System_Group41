from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""
    stations = build_station_list() # list of stations
    cam = (52.2053, 0.1218) # Cambridge city centre coordinate
    #print(stations)
    radius=10
    list = stations_within_radius(stations, cam, radius) 
    #print(list)
    by_d=[i[0] for i in list]
    print('Sorted by distance   :'+'   '.join(map(str,by_d)))
    print('Sorted Alphabetically')
    ap=sorted(by_d)
    print(ap)
run()