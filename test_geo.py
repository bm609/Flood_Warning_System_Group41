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

#Code for 1C
from floodsystem.geo import stations_within_radius
def test_stations_within_radius():
    coord=[(0,0),(0.01,0.001),(3,0),(0,0.001)]
    
    from haversine import haversine
    
    # 0:ID, 1:ID, 2:NAME, 3:COORDINATE 4:TYPICAL RANGE, 5:RIVER, 6:TOWN
    stationA = MonitoringStation("TestA0", "TestA1", "TestA2", coord[0], "TestA4", "TestA5","TestA6")
    stationB = MonitoringStation("TestB0", "TestB1", "TestB2", coord[1], "TestB4", "TestB5","TestB6")
    stationC = MonitoringStation("TestC0", "TestC1", "TestC2", coord[2], "TestC4", "TestC5","TestC6")
    stationD = MonitoringStation("TestD0", "TestD1", "TestD2", coord[3], "TestD4", "TestD5","TestD6")
    stations_test=[stationA,stationB,stationC,stationD]
    centre = (0,0)
    print()
    r=10
    output=stations_within_radius(stations_test, centre, r)
    assert type(output) == list
    print(output)
    #Names are Test_n_2 variables
    assert output[0][0]=='TestA2'
    assert output[1][0]=='TestD2'
    assert output[2][0]=='TestB2'

#code for 1E

def test_rivers_by_station_number():

    from floodsystem.geo import rivers_by_station_number


    # 0:ID, 1:ID, 2:NAME, 3:COORDINATE 4:TYPICAL RANGE, 5:RIVER, 6:TOWN
    stationA = MonitoringStation("TestA0", "TestA1", "TestA2","TestA3", "TestA4", "River 1","TestA6")
    stationB = MonitoringStation("TestB0", "TestB1", "TestB2","TestB3", "TestB4", "River 1","TestB6")
    stationC = MonitoringStation("TestC0", "TestC1", "TestC2","TestC3", "TestC4", "River 0","TestC6")
    stationD = MonitoringStation("TestD0", "TestD1", "TestD2","TestD3", "TestD4", "River 2","TestD6")
    stations_test=[stationA,stationB,stationC,stationD]
    N=2
    output=rivers_by_station_number(stations_test, N)
    assert output==[('River 1', 2), ('River 2', 1)]