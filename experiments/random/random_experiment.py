from code.classes import route
from code.classes import network
from code.algorithms.greedy import RandomGreedy
from code.visualisation.visualisation import Visualisation
import copy
import matplotlib.pyplot as plt
from code.algorithms.randomised import RandomNet
from tqdm import tqdm
from code.algorithms.heuristics.heuristics import max_connections_heuristic, unique_connections_heuristic, distance_based_heuristic
import csv 
import pickle 

def random(network_obj, all_stations, ammount_of_routes, runs=10000):
        
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
    plt.show()



def random_vis(file): 
    network_data = open('results/random/network_data', 'rb')
    data = pickle.load(network_data) 
    network_data.close()

    vis = Visualisation()
    vis.extract_data(f'data/Stations{file}.csv', f'data/Connecties{file}.csv')
    vis.visualise(data.network)