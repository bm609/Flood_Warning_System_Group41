"""Unit test for geo module"""

from distutils.command.build_clib import build_clib
import string
from numpy import test
from floodsystem.geo import stations_by_distance, stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    stationA = MonitoringStation("TestA", "TestA", "TestA", (2,2), None, "TestA", "TestA")
    stationB = MonitoringStation("TestB", "TestB", "TestB", (3,3), None, "TestB", "TestB")
    s = [stationA, stationB]
    A = stations_by_distance(s, (0,0))
    assert A[0] == ("TestA", "TestA", 314.47523947196964)   #coordinate calculated using haversine formula, testing to make sure A is first
                #also tests for output to be the right format; tuple (string, string, float)

def test_rivers_with_station():
    test = build_station_list()
    test = rivers_with_station(test)
    assert type(test) == set  #checks if datatype of output is set. If true, no duplicates can be
                                                    #present (as datatype is a set)

def test_stations_by_river():
    station = build_station_list()
    riverlist = stations_by_river(station)
    assert type(riverlist) == dict #check if stations_by_river output is dict
    for rivers in station:
        assert len(riverlist[rivers.river]) > 0 #checks that each river has at least 1 station

