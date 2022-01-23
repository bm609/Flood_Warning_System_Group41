# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit #importing haversine library for distance calculations
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    station_dist = []   #initialise list
    for i in stations:
        station_dist.append((i.name, i.town, haversine(i.coord, p))) #add current iterations station name, town, and distance. haversine default unit is km
    station_dist.sort(key = lambda x: x[2]) #sorts list by third element (the distance) represented by x[2]
    return station_dist
    
def rivers_with_station(stations):
    riverstation = set()   #initialise set
    for i in stations:
        riverstation.add(i.river) #adds river name to set for every station
    riverlist = sorted(riverstation)  #converts set into sorted list (alphabetical) for clarity
    return riverlist

def stations_by_river(stations):
    riverstation = {}       #riverstation dict
    rivers = rivers_with_station(stations) #creates list of rivers
    for i in rivers:            #creates a key of the river's name for each river in rivers
        riverstation[i] = []    #empty list given as value, so that append may be used
    for i in stations:
        riverstation[i.river].append(i.name) #appends station name to respective river for every station
    return riverstation

    