from code.classes import route
from code.classes import network
from code.algorithms.greedy import RandomGreedy
from code.visualisation.visualisation import Visualisation
import copy
import matplotlib.pyplot as plt
from code.algorithms.randomised import RandomNet
from tqdm import tqdm
from code.algorithms.heuristics.heuristics import max_connections_heuristic, unique_connections_heuristic, distance_based_heuristic

def run_random(network_obj, all_stations, greedy=False, ammount_of_routes=7,
                   runs=10000, hist_view=False, vis=False):
    '''
    IN: - network_obj: empty Network-Class object
        - all_stations: list of Station objects
        - greedy: if True compute RandomGreedy
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
        if greedy:
            random_net = RandomGreedy(all_stations, network_obj.total_tracks, network_obj)
            random_net.run(unique_connections_heuristic)
        else:
            random_net = RandomNet(network_obj, all_stations, ammount_of_routes, timeframe)
            random_net.run()
        quality = random_net.network.quality()
        k_values.append(quality)

        # save the best k and the corresponding Network instance 
        if quality > best_k: 
            best_k = quality 
            best_network = copy.deepcopy(random_net)
    print(f"With {best_network.network.ammount_of_routes} route(s) the best K is: {best_k}")


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
        csv_file_stations = f'data/Stations{file}.csv' 

        # Create list with connections
        csv_file_connections = f'data/Connecties{file}.csv'

        vis = Visualisation()
        vis.extract_data(csv_file_stations, csv_file_connections)

        vis.visualise(best_network.rail_net)

def run_greedy(algorithm, vis=False, iterations=1000):
    best_network = None
    best_quality = -10000


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
            csv_file_stations = f'data/Stations{file}.csv' 

            # Create list with connections
            csv_file_connections = f'data/Connecties{file}.csv'

            vis = Visualisation()
            vis.extract_data(csv_file_stations, csv_file_connections)

            vis.visualise(best_network)