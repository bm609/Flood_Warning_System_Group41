
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

def stations_highest_rel_level(stations, N):
    """"returns a list of the N stations with highest relative water levels"""
    statlist = []                                                #
    for i in stations:                                           #
        if i.relative_water_level() == None:                     #
            next                                                 # could replace with stations_level_over_threshold with tol = small no. (-ve)
        else:                                                    #  this way feels more correct
            statlist.append((i, i.relative_water_level()))       #
    statlist.sort(key = lambda x: x[1], reverse=True)            #
    Nlist =[]
    for i in range(0, N):
        Nlist.append(statlist[i][0])                         #appends ith term from 0-N for statlist, but only the 0th element (MonitoringStation object)
    return Nlist