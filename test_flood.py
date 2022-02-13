"""Unit test for flood module."""

from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    testA = MonitoringStation("A","","","",[1,2],"","")
    testB = MonitoringStation("B","","","",[1,2],"","")  
    testC = MonitoringStation("C","","","",[1,2],"","")  
    testD = MonitoringStation("D","","","",[1,2],"","")  

    testA.latest_level = 4
    testB.latest_level = 6  
    testC.latest_level = 5 
    testD.latest_level = 3
    testE = MonitoringStation("E","","","",None,"","") # check to see if discounted
    stations = [testA, testB, testC, testD, testE]
    reslist = stations_level_over_threshold(stations, 2)
    assert type(reslist) == list  #checking type of output
    assert type(reslist[0]) == tuple #checking type of list element
    assert reslist[0] == (testB, 5) #checking output list is sorted, and gives right output
    assert len(reslist) == 3 #checking that testD & E are removed to give length of 3
