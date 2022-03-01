"""Unit test for flood module."""

from matplotlib import dates
from floodsystem.stationdata import build_station_list
from floodsystem.flood import plot_water_levels, stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation
import numpy as np
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

def test_stations_highest_rel_level():
   
    testA = MonitoringStation("A","","","",[1,2],"","")
    testB = MonitoringStation("B","","","",[1,2],"","")  
    testC = MonitoringStation("C","","","",[1,2],"","")  
    testD = MonitoringStation("D","","","",[1,2],"","")  
    testA.latest_level = 10
    testB.latest_level = 8 
    testC.latest_level = 6 
    testD.latest_level = 4
    stations = [testA,testB,testC,testD]
    output = stations_highest_rel_level(stations, 3)
    print(output)
    assert len(output) == 3 #checks only 3 are in list
    assert output[0] == testA #checks first in list is greatest rel level
    assert output[2] == testC #checks last in list smallest rel level within N

def test_plot_water_levels():
    import datetime as DT
    import matplotlib.dates as mdates
    import matplotlib.ticker as ticker
    testA = MonitoringStation("A","A","A","A",[1,2],"A","A")
    levels= np.random.randint(1,5,15)
    print(levels)
    dates = mdates.num2date(mdates.drange(DT.datetime(2022, 11, 30),
                                      DT.datetime(2022, 12, 15),
                                      DT.timedelta(days=1)))
    plot_water_levels(testA, dates, levels)
#seems difficult to test, as output is graph
#this test just shows the plotting works
