from code.visualisation.visualisation import Visualisation
import copy
import matplotlib.pyplot as plt
from code.algorithms.greedy import Greedy, RandomGreedy, SemiRandomGreedy
from tqdm import tqdm
import csv 
import pickle 
import random

def greedy(all_stations, network_obj, heuristic):
    greedy_net = Greedy(all_stations, network_obj.total_tracks, network_obj)
    greedy_net.run(heuristic)
    network_data = open(f"results/greedy/network_data_{heuristic.__name__}", 'wb')
    pickle.dump(greedy_net, network_data)
    network_data.close()


def random_greedy(network_obj, all_stations, heuristic, runs=10000):
    '''
    IN: - network_obj: empty Network-Class object
        - all_stations: list of Station objects
        - greedy: if True compute RandomGreedy
        - runs: ammount of runs for the experiment
        - hist_view: Boolean to show a histogram
        - vis: Boolean to show the map visualisation
    ammount_of_routes choices:
        - 7
        - 20
    '''    
    
    # initialising parameters for experiment 
    best_k = 0 
    best_network = None

    with open("results/greedy/random_greedy_data.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')    

        for t in tqdm(range(runs)):
            random.seed(t) # seed added
            random_net = RandomGreedy(all_stations, network_obj.total_tracks, network_obj)
            random_net.run(heuristic)
            quality = random_net.network.quality()
            result_writer.writerow([int(quality)])
            
            # save the best k and the corresponding Network instance 
            if quality > best_k: 
                best_k = quality 
                best_network = copy.deepcopy(random_net)
                network_data = open('results/greedy/random_greedy/network_data', 'wb')
                pickle.dump(best_network, network_data)
                network_data.close()



def random_greedy_graph(): 


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
    if random:
        network_data = open('results/greedy/random_greedy/network_data', 'rb')

    elif heuristic:
        network_data = open(f'results/greedy/network_data_{heuristic.__name__}', 'rb')

    else:
        raise Warning("No network data available for a visualisation")
    
    data = pickle.load(network_data) 
    network_data.close()
    print(f"The quality of this network is {data.network.quality()}")

    vis = Visualisation()
    vis.extract_data(f'data/Stations{file}.csv', f'data/Connecties{file}.csv')
    vis.visualise(data.network)