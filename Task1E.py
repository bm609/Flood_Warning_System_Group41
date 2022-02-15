from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task E"""
    stations = build_station_list() # list of stations
    number=9
    answer,no_of_data=rivers_by_station_number(stations,number)
    
    print('{} data extracted'.format(no_of_data))
    if no_of_data>number:
        print('Extra entries presented due to repeated values')
    print(answer)
    
run() 

   # return output
