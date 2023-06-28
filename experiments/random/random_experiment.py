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
        - ammount_of_routes: maximum routes in a network
        - runs: ammount of runs for the experiment
    ammount_of_routes choices:
        - 7
        - 20
    This function creates multiple random networks for a randomise experiment.
    In this function the best network out of runs amount of networks will be
    saved in a pickle file. Each networks quality value is written to a csv for
    further investigation.
    '''    

    # initialising parameters for experiment 
    best_k = 0 
    best_network = None

    # automatically choose the timeframe for the routes
    if ammount_of_routes == 7: 
        timeframe = 120 
    else: 
        timeframe = 180

    with open("results/random/random_data.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')    

        # run the experiment runs amount of times
        for t in tqdm(range(runs)):

            # use a random seed for validation of the experiment later on
            random.seed(t)
            random_net = RandomNet(network_obj, all_stations, ammount_of_routes, timeframe)
            random_net.run()
            quality = random_net.network.quality()
            result_writer.writerow([int(quality)])
            
            # save the best k and the corresponding Network instance 
            if quality > best_k: 
                best_k = quality 
                best_network = copy.deepcopy(random_net)

    # put the best network instance in a pickle file    
    network_data = open('results/random/network_data', 'wb')
    pickle.dump(best_network, network_data)
    network_data.close()



def random_graph(): 
    """
    This function draws a histogram out of the qualities that have been
    written into the csv in the random_net function. It saves the histogram
    to a specific destination.  
    """
    results = []
    with open("results/random/random_data.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        for k_value in result_reader:
            results.append(int(k_value[0]))

    plt.hist(results, bins = 1000)
    plt.xlabel('Value for K')
    plt.ylabel('Ammount')
    plt.xlim(0, 10000)
    plt.ylim(0, 120)
    plt.title('Values for K using the Randomized algorithm') 
    plt.savefig(f'results/random/Histogram_Random.png')
    plt.show()



def random_vis(file): 
    """
    IN: - file: string that represents Holland or Nationaal
    This function visualises the best network that was written
    into the pickle file in the random_net function.
    """
    network_data = open('results/random/network_data', 'rb')
    data = pickle.load(network_data) 
    network_data.close()
    print(data.network.quality())

    vis = Visualisation()
    vis.extract_data(f'data/Stations{file}.csv', f'data/Connecties{file}.csv')
    vis.visualise(data.network)