from classes import route
from classes import network
from visualisation.visualisation import *
import copy
import matplotlib.pyplot as plt
from tqdm import tqdm

def run_algorithm(algorithm, ammount_of_routes=7, runs=10000, all_stations=None, connections=None):

#----------------- EXPERIMENT: RANDOMIZED -----------------
    best_ks = list()
    unique_tracks = []


    # initialising parameters for experiment 
    runs = 100000
    k_values = []
    best_k = 0 
    best_network = None
    heuristic = 'unique_based'

    for t in tqdm(range(runs)):

        # initialise a network, give it the total ammount of connections  
        rail_net = network.Network(len(connections), ammount_of_routes)

        for r in range(1,ammount_of_routes+1): 

            # initialise a route-object and computing the route 
            new_route = route.Route(120, all_stations) 
            algorithm(new_route, rail_net).build_route(heuristic)
            new_route.compute_covered_connections()
            
            # add the route and the unique connections to the network 
            rail_net.add_route(new_route, new_route.connection_set)
            rail_net.calculate_unique_connections()
        
            if len(rail_net.unique_tracks) == rail_net.total_tracks:
                rail_net.ammount_of_routes = r
                break

        # identify all unique connections in the network 
        rail_net.calculate_unique_connections()
        unique_tracks.append(len(rail_net.unique_tracks))
        # calculate the quality of the network 
        quality = rail_net.quality()

        k_values.append(quality)

        # save the best k and the corresponding Network instance 
        if quality > best_k: 
            best_k = quality 
            best_network = copy.deepcopy(rail_net)
    best_ks.append(f"With {best_network.ammount_of_routes} route(s) the best K is: {best_k}")
    print(best_ks)


#----------------- EXPERIMENT VISUALISATION -----------------
plt.hist(k_values, bins = 1000)
plt.xlabel('Value for K')
plt.ylabel('Ammount')
plt.title('Values for K using the Randomized algorithm')
plt.savefig(f'code/visualisation/plots/Histogram_{heuristic}.png') # maar 1 keer gebruiken denk ik?
plt.show

#----------------- NETWORK VISUALISATION -----------------
# Create list with stations
csv_file = 'data/StationsHolland.csv' 
station_list_holland = extract_stations(csv_file)

# Create list with connections
csv_file_connections = 'data/ConnectiesHolland.csv'
connections_holland = read_connections(csv_file_connections)

visualise(station_list_holland, connections_holland, best_network)
