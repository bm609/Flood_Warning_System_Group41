# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit #importing haversine library for distance calculations
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    station_dist = []
    for i in range(len(stations)):
        station_dist.append((stations[i].name, stations[i].town, haversine(stations[i].coord, p))) #add current iterations station name, town, and distance. haversine default unit is km
    station_dist.sort(key = lambda x: x[2]) #sorts list by third element (the distance) represented by x[2]
    return station_dist
    