from os import times

from matplotlib.pyplot import title


def stations_level_over_threshold(stations, tol):
    """returns a list of tuples (MonitoringStation, MonitoringStation.relative_water_level) where 
        all relative water levels are > tol"""
    statlist = []
    for i in stations:
        if i.relative_water_level() == None:  # discounts all invalid data
            next
        elif i.relative_water_level() > tol:
            statlist.append((i, i.relative_water_level()))
    statlist.sort(key=lambda x: x[1], reverse=True)  # sorts list by 2nd element (relative water level)
    return statlist


def stations_highest_rel_level(stations, N):
    """"returns a list of the N stations with highest relative water levels"""
    statlist = []  #
    for i in stations:  #
        if i.relative_water_level() == None:  #
            next  # could replace with stations_level_over_threshold with tol = small no. (-ve)
        else:  # this way feels more correct, as no exceptions.
            statlist.append((i, i.relative_water_level()))  #
    statlist.sort(key=lambda x: x[1], reverse=True)  #
    Nlist = []
    for i in range(0, N):
        Nlist.append(statlist[i][
                         0])  # appends ith term from 0-N for statlist, but only the 0th element (MonitoringStation object)
    return Nlist


def plot_water_levels(station, dates, levels):
    """displays a plot of 'station' water 'levels' over the past 'dates' days"""
    import matplotlib.pyplot as plt
    lower_range = [station.typical_range[0]] * len(dates)  # creating lists for straight line plot
    upper_range = [station.typical_range[1]] * len(dates)
    plt.plot(dates, levels)
    plt.plot(dates, lower_range, '--', label="Lower range")  # adding lower range line (dotted)
    plt.plot(dates, upper_range, '--', label="Upper range")  # adding upper range line (dotted)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    if len(dates) == 0:
        plt.title(station.name + " : No Recent Data Available")  # makes clear if no data available - still shows graph.
    plt.legend()
    plt.tight_layout()
    plt.show()

def polyfit(dates, levels, p):
    """displays a plot of 'station' water 'levels' over the past 'dates' days"""
    import numpy as np
    import matplotlib.pyplot as plt
    from datetime import datetime
    x = []

    for i in range(len(dates)):
        x.append(dates[i].timestamp())

    y = levels

    xx = np.asarray(x)

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4

    if levels != [] and dates != []:
        # Using shifted x values, find coefficient of best-fit
        # polynomial f(x) of degree p
        p_coeff = np.polyfit(xx - xx[0], y, p)

        poly = np.poly1d(p_coeff)

        # Plot polynomial fit at 30 points along interval (note that polynomial

        x1 = np.linspace(xx[0], xx[-1], 30)

        xt = []
        for i in range(30):
            xt.append(datetime.fromtimestamp(x1[i]))

        x1 = np.linspace(xx[0], xx[-1], 30)
        plt.plot(xt, poly(x1 - x1[0]), label="line of best fit")
    else:
        pass

    # Display plot
    # plt.xticks(rotation=45)
    # plt.legend()
    # plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """displays a plot of 'station' water 'levels' over the past 'dates' days"""
    import matplotlib.pyplot as plt
    lower_range = [station.typical_range[0]] * len(dates)  # creating lists for straight line plot
    upper_range = [station.typical_range[1]] * len(dates)
    if dates:
        polyfit(dates, levels, p)
    plt.plot(dates, levels, label="water level")
    plt.plot(dates, lower_range, '--', label="Lower range")  # adding lower range line (dotted)
    plt.plot(dates, upper_range, '--', label="Upper range")  # adding upper range line (dotted)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()
    plt.tight_layout()
    plt.show()
