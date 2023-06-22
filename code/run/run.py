from code.classes import route
from code.classes import network
from code.visualisation.visualisation import *
import copy
import matplotlib.pyplot as plt
from code.algorithms.randomised import RandomRoute
from tqdm import tqdm

def run_random(all_stations, connections, ammount_of_routes=7,
                   runs=10000, hist_view=False, vis=False):
    '''
    IN: - all_stations: list of Station objects
        - connections: connections DataFrame
        - ammount_of_routes: maximum routes in a network
        - runs: ammount of runs for the experiment
        - hist_view: Boolean to show a histogram
        - vis: Boolean to show the map visualisation
    ammount_of_routes choices:
        - 7
        - 20
    '''

#----------------- EXPERIMENT: RANDOMIZED -----------------
    if ammount_of_routes == 7:
        timeframe = 120
        file = 'Holland'
    elif ammount_of_routes == 20:
        timeframe = 180
        file = 'Nationaal'

    # initialising parameters for experiment 
    k_values = []
    best_k = 0 
    best_network = None

    for t in tqdm(range(runs)):

        # initialise a network, give it the total ammount of connections  
        rail_net = network.Network(len(connections), ammount_of_routes)

        for r in range(1,ammount_of_routes+1): 

            # initialise a route-object and computing the route 
            new_route = route.Route(timeframe, all_stations, r) 
            RandomRoute(new_route).build_route()
            new_route.compute_covered_connections()
            
            # add the route and the unique connections to the network 
            rail_net.add_route(new_route, new_route.connection_set)
            rail_net.calculate_unique_connections()
        
            if len(rail_net.unique_tracks) == rail_net.total_tracks:
                rail_net.ammount_of_routes = r
                break

        # identify all unique connections in the network 
        rail_net.calculate_unique_connections()

        # calculate the quality of the network 
        quality = rail_net.quality()

        k_values.append(quality)

        # save the best k and the corresponding Network instance 
        if quality > best_k: 
            best_k = quality 
            best_network = copy.deepcopy(rail_net)
    print(f"With {best_network.ammount_of_routes} route(s) the best K is: {best_k}")


    #----------------- EXPERIMENT VISUALISATION -----------------
    if hist_view:
        plt.hist(k_values, bins = 1000)
        plt.xlabel('Value for K')
        plt.ylabel('Ammount')
        plt.title('Values for K using the Randomized algorithm') 
        plt.savefig(f'code/visualisation/plots/Histogram_Random_{ammount_of_routes}_routes.png')
        plt.show()
            
    if vis:
        #----------------- NETWORK VISUALISATION -----------------
        # Create list with stations
        csv_file = f'data/Stations{file}.csv' 
        stations_list = extract_stations(csv_file)

        # Create list with connections
        csv_file_connections = f'data/Connecties{file}.csv'
        connections_list = read_connections(csv_file_connections)

        visualise(stations_list, connections_list, best_network)

def run_greedy(algorithm, vis=False, iterations=1000):
    best_network = None
    best_quality = 0

    for t in tqdm(range(iterations)):
        network = copy.deepcopy(algorithm.rail_net)
        if network.quality() > best_quality:
            best_network = network
            best_quality = network.quality()

    print(best_quality, len(best_network.unique_tracks))

    if network.ammount_of_routes == 7:
        file = 'Holland'
    elif network.ammount_of_routes == 20:
        file = 'Nationaal'

    if vis:
            #----------------- NETWORK VISUALISATION -----------------
            # Create list with stations
            csv_file = f'data/Stations{file}.csv' 
            stations_list = extract_stations(csv_file)

            # Create list with connections
            csv_file_connections = f'data/Connecties{file}.csv'
            connections_list = read_connections(csv_file_connections)

            visualise(stations_list, connections_list, best_network)    
