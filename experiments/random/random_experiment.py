from code.classes import route
from code.classes import network
from code.visualisation.visualisation import Visualisation
import copy
import matplotlib.pyplot as plt
from code.algorithms.randomised import RandomNet
from tqdm import tqdm
import csv 
import pickle 
import random

def random_net(network_obj, all_stations, ammount_of_routes, runs=10000):
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

    # initialising parameters for experiment 
    best_k = 0 
    best_network = None

    if ammount_of_routes == 7: 
        timeframe = 120 
    else: 
        timeframe = 180

    with open("results/random/random_data.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')    

        for t in tqdm(range(runs)):
            random.seed(t) # seed added
            random_net = RandomNet(network_obj, all_stations, ammount_of_routes, timeframe)
            random_net.run()
            quality = random_net.network.quality()
            result_writer.writerow([int(quality)])
            
            # save the best k and the corresponding Network instance 
            if quality > best_k: 
                best_k = quality 
                best_network = copy.deepcopy(random_net)
                network_data = open('results/random/network_data', 'wb')
                pickle.dump(best_network, network_data)
                network_data.close()



def random_graph(): 


    results = []
    with open("results/random/random_data.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        for k_value in result_reader:
            results.append(int(k_value[0]))

    plt.hist(results, bins = 1000)
    plt.xlabel('Value for K')
    plt.ylabel('Ammount')
    plt.xlim(0, 10000)
    plt.ylim(0, 200)
    plt.title('Values for K using the Randomized algorithm') 
    plt.savefig(f'results/randomHistogram_Random.png')
    plt.show()



def random_vis(file): 
    network_data = open('results/random/network_data', 'rb')
    data = pickle.load(network_data) 
    network_data.close()
    print(data.network.quality())

    vis = Visualisation()
    vis.extract_data(f'data/Stations{file}.csv', f'data/Connecties{file}.csv')
    vis.visualise(data.network)