from code.visualisation.visualisation import Visualisation
import copy
import matplotlib.pyplot as plt
from code.algorithms.greedy import Greedy, RandomGreedy, SemiRandomGreedy
from tqdm import tqdm
import csv 
import pickle 
import random

def greedy(all_stations, network_obj, heuristic):
    '''
    IN: - all_stations: list of Station objects
        - network_obj: empty Network-Class object
        - heuristic: heuristic choice for connections
        heuristic choices:
        - unique_connections_heuristic
        - maximum_connections_heuristic
        - distance_based_heuristic
    This function creates a Greedy network based on a choice heuristic.
    In this function the network will be saved in a pickle file for 
    visualisation.
    '''        
    if network_obj.ammount_of_routes == 7:
        file = 'Holland'
    else:
        file = 'Nationaal'

    # create a greedy instance
    greedy_net = Greedy(all_stations, network_obj.total_tracks, network_obj)
    greedy_net.run(heuristic)

    # put the greedy class in a pickle file
    network_data = open(f"results/greedy/network_data_{file}_{heuristic.__name__}", 'wb')
    pickle.dump(greedy_net, network_data)
    network_data.close()


def random_greedy(network_obj, all_stations, heuristic, runs=10000):
    '''
    IN: - network_obj: empty Network-Class object
        - all_stations: list of Station objects
        - heuristic: heuristic choice for connections
        - runs: ammount of runs for the experiment
        heuristic choices:
        - unique_connections_heuristic
        - maximum_connections_heuristic
        - distance_based_heuristic
    This function creates multiple Random Greedy networks for a randomise experiment.
    In this function the best network out of runs amount of networks will be
    saved in a pickle file. Each networks quality value is written to a csv for
    further investigation.
    '''    
    
    # initialising parameters for experiment 
    best_k = 0 
    best_network = None

    with open("results/greedy/random_greedy_data.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')    

        # run the experiment runs amount of times
        for t in tqdm(range(runs)):

            # use a random seed for validation of the experiment later on
            random.seed(t) 
            random_net = RandomGreedy(all_stations, network_obj.total_tracks, network_obj)
            random_net.run(heuristic)
            quality = random_net.network.quality()
            result_writer.writerow([int(quality)])
            
            # save the best k and the corresponding Network instance 
            if quality > best_k: 
                best_k = quality 
                best_network = copy.deepcopy(random_net)

        # put the best network instance in a pickle file         
        network_data = open('results/greedy/random_greedy/network_data', 'wb')
        pickle.dump(best_network, network_data)
        network_data.close()

def heuristic_differences(file):
    bars = list()
    heuristics = list()
    network_data = open(f'results/greedy/network_data_{file}_unique_connections_heuristic', 'rb')
    unique_data = pickle.load(network_data)
    network_data.close()
    bars.append(unique_data.network.quality())
    heuristics.append('unique_connections_heuristic')

    network_data = open(f'results/greedy/network_data_{file}_max_connections_heuristic', 'rb')
    max_data = pickle.load(network_data)
    network_data.close()
    bars.append(max_data.network.quality())
    heuristics.append('max_connections_heuristic')

    network_data = open(f'results/greedy/network_data_{file}_distance_based_heuristic', 'rb')
    distance_data = pickle.load(network_data)
    network_data.close()
    bars.append(distance_data.network.quality())
    heuristics.append('distance_based_heuristic')

    plt.bar(heuristics, bars) # give bars different colors change names so that it is readable(maybe in a legend?)
    plt.ylim(0, 10000)
    plt.show()

    
def random_greedy_graph(): 
    """
    This function draws a histogram out of the qualities that have been
    written into the csv in the random_greedy function. It saves the histogram
    to a specific destination.  
    """
    results = []
    with open("results/greedy/random_greedy_data.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        for k_value in result_reader:
            results.append(int(k_value[0]))

    plt.hist(results, bins = 1000)
    plt.xlabel('Value for K')
    plt.ylabel('Ammount')
    plt.xlim(0, 10000)
    plt.ylim(0, 200)
    plt.title('Values for K using the Randomized algorithm') 
    plt.savefig(f'results/greedy/random_greedy/Histogram_Random_greedy.png')
    plt.show()



def greedy_vis(file, heuristic=None, random=False): 
    """
    IN: - file: string that represents Holland or Nationaal
        - heuristic: used to open the specific heuristic greedy map
        - random: bool used to open the best random greedy network
    This function visualises the best network that was written
    into the pickle file in the random_net function.
    """    
    if random:
        network_data = open('results/greedy/random_greedy/network_data', 'rb')

    elif heuristic:
        network_data = open(f'results/greedy/network_data_{file}_{heuristic.__name__}', 'rb')

    else:
        raise Warning("No network data available for a visualisation")
    
    data = pickle.load(network_data) 
    network_data.close()
    print(f"The quality of this network is {data.network.quality()}")

    vis = Visualisation()
    vis.extract_data(f'data/Stations{file}.csv', f'data/Connecties{file}.csv')
    vis.visualise(data.network)