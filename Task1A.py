# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1A"""

    class MonitoringStation:
        def __init__(self,Station_ID,Measurement_ID,Name,Geographic_coordinate,Typical_low_high_levels,River_on_which_the_station_is_located,Closest_town_to_the_station):
            self.Station_ID=Station_ID
            self.Measurement_ID=Measurement_ID
            self.Name=Name
            self.Geographic_coordinate=Geographic_coordinate
            self.Typical_low_high_levels=Typical_low_high_levels
            self.River_on_which_the_station_is_located=River_on_which_the_station_is_located
            self.Closest_town_to_the_station=Closest_town_to_the_station
        def __repr__(self):
            rep= 'Station ID: {},Measurement ID: {},Name: {},Geographic coordinate: {},Typical low/high levels: {},River on which the station is located: {},Closest town to the station: {}'.format(self.Station_ID,self.Measurement_ID,self.Name,self.Geographic_coordinate,self.Typical_low_high_levels,self.River_on_which_the_station_is_located,self.Closest_town_to_the_station)
            return rep

    
    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    # Display data from 3 stations:
    for station in stations:
        if station.name in [
                'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge'
        ]:
            print(station)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

#Test
