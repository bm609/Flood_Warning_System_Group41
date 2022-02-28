import datetime
from floodsystem.flood import stations_level_over_threshold, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    rel = stations_level_over_threshold(stations, 1.3) #all stations with rel level >1.3 (significantly above usual high)
    print(rel)
    for i in rel:
        dates, levels = fetch_measure_levels(i[0].measure_id, datetime.timedelta(days=2))
        if i[0].town == None:
            next
        elif i[0].name == None:
            next
        else:
            print( i[0].name +": "+ i[0].town)
        #plot_water_level_with_fit(i[0], dates, levels, 5)

        #looking at graphs, evaluate what flood risk category to put into
        # if levels have been high consistently, risk is lower, as flooding would've likely already occured if it is capable of flooding.
        # any sharp increase (over short time period) should increase flood risk, as sudden strain on rivers / flood defenses.
        #inbetween cases (neither sustained highs or sharp rise) should be evaluated on basis of relative levels

        #Letcombe Bassett - no judgement can be made, as not enough data available, but extremely likely station faults (relative level of 666 not realistic)
        #Hayes Basin - Low - steadily falling water level, although is still significantly above normal
        #Orleton Millbrook Way - Moderate - recent sharp increase in water level, has not yet peaked, lessened by low absolute water level
        #Hull Hessle Astral Close - Moderate - same as above
        #Upper Pound - Moderate - appears to be rising fairly sharply, but below recent peak levels currently
        #Calthorpe Park - Severe - huge spike in water level over short time period
        #Stoke Prior - Moderate
        #Ferrybridge Fishergate - Moderate
        # Sandhurst Horn's Ditch - Low
        # Cheswick Green - Moderate
        #Stainland Board Mills - Moderate
        # Windyridge Road - Moderate
        #Oulton St Aidans - Low
        #Horsforth Cornmill View - Low
        #Rawcliffe - Low
        #Smithy Houses - High
        #Solihull Lodge - High
        #Shifnal - Moderate
        #West Holme Washlands - Low
        #Bescot - Low - High and sharp, but appears to have peaked already
        #Perry Park - High

        #Towns -- less as some stations do not have towns

        #Alberbury - Low 
        #Astral Close - Moderate 
        #Tewkesbury - Moderate 
        #Edgbaston - Severe 
        #Stoke Prior - Moderate
        #Maisemore - Low
        # Cheswick Green - Moderate
        #Stainland Board Mills - Moderate
        #Cheltenham - Moderate
        #Oulton St Aidans - Low
        #Horsforth Cornmill View - Low
        #Rawcliffe - Low
        #Major's Green - High
        #Shifnal - Moderate
        #West Holme Washlands - Low
        #Perry Barr - High
run()
