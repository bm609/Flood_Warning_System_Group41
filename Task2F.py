import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import plot_water_level_with_fit, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    highstat = stations_highest_rel_level(stations, 5)
    p = 4
    for i in highstat:
        dates, levels = fetch_measure_levels(i.measure_id, datetime.timedelta(days=2))
        plot_water_level_with_fit(i, dates, levels, p)


run()

# Letcombe Bassett will return an empty graph
# No recent data recorded
# As the program displays recent data, the blank graph is correct
# https://check-for-flooding.service.gov.uk/station/7079 shows lack of data for Letcombe Bassett
