from os import times

from matplotlib.pyplot import title

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
        else:                                                    #  this way feels more correct, as no exceptions.
            statlist.append((i, i.relative_water_level()))       #
    statlist.sort(key = lambda x: x[1], reverse=True)            #
    Nlist =[]
    for i in range(0, N):
        Nlist.append(statlist[i][0])                         #appends ith term from 0-N for statlist, but only the 0th element (MonitoringStation object)
    return Nlist

def plot_water_levels(station, dates, levels):
    """displays a plot of 'station' water 'levels' over the past 'dates' days"""
    import matplotlib.pyplot as plt
    lower_range = [station.typical_range[0]]*len(dates) #creating lists for straight line plot
    upper_range = [station.typical_range[1]]*len(dates) 
    plt.plot(dates, levels)
    plt.plot(dates, lower_range, '--', label = "Lower range") #adding lower range line (dotted)
    plt.plot(dates, upper_range, '--', label = "Upper range") #adding upper range line (dotted)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend
    plt.tight_layout()  
    plt.show()