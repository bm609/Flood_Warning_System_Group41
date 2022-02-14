import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import plot_water_levels, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highstat = stations_highest_rel_level(stations, 2)
    #del highstat[0]
    for i in highstat:
        dates, levels = fetch_measure_levels(i.measure_id, datetime.timedelta(days=10))
        print(dates)
        print(levels)
        plot_water_levels(i, dates, levels)
run() #Letcombe Bassett will return an empty graph
        #this is as there is no recent data recorded
        #as the program displays recent data, the blank graph is correct
        # https://check-for-flooding.service.gov.uk/station/7079 shows lack of data for Letcombe Bassett