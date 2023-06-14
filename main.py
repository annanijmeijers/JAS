import pandas as pd 
import csv 
from code.classes import station 
from code.classes import route 
from code.classes import network 
from code.algorithms import randomised 

if __name__ == "__main__":
    
    # load the data 
    df_connections = pd.read_csv('data/ConnectiesHolland.csv')
    df_stations = pd.read_csv('data/StationsHolland.csv')
    
    # initialising a csv-file to write the results to 
    f = open('rail_network.csv', 'w')
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['route', 'station'])

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
        # storing available connections to each station 
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

    ammount_of_routes = 3

    # initialise a network, give it the total ammount of connections  
    rail_net = network.Network(len(df_connections), ammount_of_routes)

    for r in range(1,ammount_of_routes+1): 

        # initialise a route-object and computing the route 
        new_route = route.Route(60, all_stations) 
        randomised.build_route(new_route)
        new_route.compute_covered_connections()
        
        # add the route and the unique connections to the network 
        rail_net.add_route(new_route, new_route.connection_set)

        writer.writerow([f'route_{r}', new_route.route])

    # identify all unique connections in the network 
    rail_net.calculate_unique_connections()

    # calculate the quality of the network 
    quality = rail_net.quality()

    writer.writerow(['score', quality])
    f.close()

    # for  visualize: to get the route per Route-object, call: rail_net.routes to get a list of Route-objects.
    # per object call route.route 
