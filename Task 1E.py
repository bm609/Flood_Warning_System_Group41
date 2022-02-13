from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task E"""
    stations = build_station_list() # list of stations
    number=9
    answer=rivers_by_station_number(stations,number)
    
    
    print(answer)
    
run()

   # return output
