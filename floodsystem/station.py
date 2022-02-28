# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""





class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """method which returns false if the typical range attribute is not in the form (low range, highrange) where 
         highrange > lowrange """
        if self.typical_range == None:      #if the type is none
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            return True
        
    def relative_water_level(self):
        """ method returns latest water level as fraction of typical range"""
        if self.typical_range_consistent() == False:  #if inconsistent range data, return none
            return None
        elif self.latest_level == None:  #if no current level, return none 
            return None
        else:
            levelrange = self.typical_range[1] - self.typical_range[0]   #high range - low range
            relative_level = (self.latest_level - self.typical_range[0])/levelrange  #divides level above typical low by range to give fraction
            #will give 0 for latest_level = lower range, -ve for less
            return relative_level
       

def inconsistent_typical_range_stations(stations):
    """input of list of monitoring station type. output of list of all monitoring station class having iconsistent range data,
     as determined by the typical_range_consistent method."""
    incon = []
    for i in stations:       #for each station, check validity of range and append if invalid
        if i.typical_range_consistent() == False:
            incon.append(i)
    return incon