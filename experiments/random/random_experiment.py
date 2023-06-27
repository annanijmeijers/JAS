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


# initialising parameters for experiment 
k_values = []
best_k = 0 
best_network = None
with open("code/run/run_rand.csv", 'w', newline='') as output_file:
    result_writer = csv.writer(output_file, delimiter=',')    
    for t in tqdm(range(runs)):
        if greedy:
            random_net = RandomGreedy(all_stations, network_obj.total_tracks, network_obj)
            random_net.run(unique_connections_heuristic)
        else:
            random_net = RandomNet(network_obj, all_stations, ammount_of_routes, timeframe)
            random_net.run()
        quality = random_net.network.quality()
        k_values.append(quality)
        result_writer.writerow([int(quality)])
        

        # save the best k and the corresponding Network instance 
        if quality > best_k: 
            best_k = quality 
            best_network = copy.deepcopy(random_net)
print(f"With {best_network.network.ammount_of_routes} route(s) the best K is: {best_k}")
