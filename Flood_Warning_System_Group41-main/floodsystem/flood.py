
def stations_level_over_threshold(stations, tol):
    """returns a list of tuples (MonitoringStation, MonitoringStation.relative_water_level) where 
        all relative water levels are > tol"""
    statlist = []
    for i in stations:
        if i.relative_water_level() == None:  #discounts all invalid data
            next
        elif i.relative_water_level() > tol:
            statlist.append((i, i.relative_water_level()))
    statlist.sort(key = lambda x: x[1], reverse=True) #sorts list by 2nd element (relative water level)
    return statlist
