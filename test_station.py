# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    test1 = MonitoringStation("","","","",None,"","")
    test2 = MonitoringStation("","","","",[2.5,1.5],"","")
    test3 = MonitoringStation("","","","",[1.5,2.5],"","")

    assert test1.typical_range_consistent() == False #tests case of typical range = none
    assert test2.typical_range_consistent() == False #tests case of lower range > upper range
    assert test3.typical_range_consistent() == True #tests case of upper range > lower range

def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    incon = inconsistent_typical_range_stations(stations)
    for i in incon:
        assert i.typical_range_consistent() == False

def test_relative_water_level():
    test1 = MonitoringStation("","","","",[1,2],"","")  #testing case latest level < lower bound
    test1.latest_level = 0
    test2 = MonitoringStation("","","","",[1,2],"","")
    test2.latest_level = 1.5  #testing regular case - expect 0<x<1 output
    test3 = MonitoringStation("","","","",[1,2],"","")
    test3.latest_level = 5 #tessting regular case - expect >1 output
    test4 = MonitoringStation("","","","",[1,2],"","") #test case with none latest level - should return none
    test5 = MonitoringStation("","","","",None,"","")  #test case with none range - should return none
    test5.latest_level = 3
    assert test1.relative_water_level() == -1
    assert test2.relative_water_level() == 0.5
    assert test3.relative_water_level() == 4
    assert test4.relative_water_level() == None
    assert test5.relative_water_level() == None
