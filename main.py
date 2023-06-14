import pandas as pd 
from tqdm import tqdm
import copy 
from code.classes import station 
from code.classes import route 
from code.classes import network 
from code.algorithms import randomised
from code.visualisation.visualisation import *
# from code.visualisation import extract_stations
# from code.visualisation import read_connections

if __name__ == "__main__":
    
#----------------- LOADING THE DATA -----------------
    df_connections = pd.read_csv('data/ConnectiesHolland.csv')
    df_stations = pd.read_csv('data/StationsHolland.csv')

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
        # storing available connections to each station 
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

#----------------- EXPERIMENT -----------------
    best_ks = list()

    for i in range(7, 8):
        # initialising parameters for experiment 
        runs = 10000
        k_values = []
        best_k = 0 
        best_network = None 

        # ammount of routes per network 
        ammount_of_routes = i

        for t in tqdm(range(runs)):

            # initialise a network, give it the total ammount of connections  
            rail_net = network.Network(len(df_connections), ammount_of_routes)

            for r in range(1,ammount_of_routes+1): 

                # initialise a route-object and computing the route 
                new_route = route.Route(120, all_stations) 
                randomised.build_route(new_route)
                new_route.compute_covered_connections()
                
                # add the route and the unique connections to the network 
                rail_net.add_route(new_route, new_route.connection_set)

            # identify all unique connections in the network 
            rail_net.calculate_unique_connections()

            # calculate the quality of the network 
            quality = rail_net.quality()

            k_values.append(quality)

            # save the best k and the corresponding Network instance 
            if quality > best_k: 
                best_k = quality 
                best_network = copy.deepcopy(rail_net)
        best_ks.append(f"With {i} route(s) the best K is: {best_k}")


print(k_values[:10])
print(best_k)
#----------------- EXPDERIMENT VISUALISATION -----------------



#----------------- NETWORK VISUALISATION -----------------
    # for  visualise: to get the route per Route-object, call: rail_net.routes to get a list of Route-objects.
    # per object call route.route 

# Create list with stations
csv_file = 'data/StationsHolland.csv' 
station_list_holland = extract_stations(csv_file)

# Create list with connections
csv_file_connections = 'data/ConnectiesHolland.csv'
connections_holland = read_connections(csv_file_connections)

visualise(station_list_holland, connections_holland, best_network)