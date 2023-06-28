import csv
import random
from tqdm import tqdm 
from code.algorithms.randomised import RandomNet
from code.algorithms.simulatedannealing import GreedyAnnealing
import matplotlib.pyplot as plt 

def greedy_annealing(file, random_network, all_stations, heuristic, iterations=1000, temperature=1000): 

    ga = GreedyAnnealing(random_network, all_stations, temperature, heuristic)

    with open(f'results/greedyannealing/greedyannealing_{file}.csv', 'w', newline='') as f: 
        writer = csv.writer(f, delimiter=',')

        for i in tqdm(range(iterations), desc='Greedy Annealing:'): 
            ga.run(1)
            writer.writerow([ga.network.quality()])
    return ga.network

# ====================== Comparing different numbers of routes ======================

def greedy_anneal_compare_routes(file, network_object, all_stations, ammount_of_routes, heuristic, iterations=1000, temperature=1000):

    for r in range(1, ammount_of_routes+1): 

        random.seed(1)
        random_algorithm = RandomNet(network_object, all_stations, r, route_time=180)
        random_algorithm.run()
        random_network = random_algorithm.network 

        ga = GreedyAnnealing(random_network, all_stations, temperature, heuristic)

        with open(f'results/greedyannealing/compare_routes/ga_{r}_routes_{file}.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            for i in tqdm(range(iterations), desc=f'Greedy Annealing, routes{r}:', leave=False): 
                ga.run(1)
                writer.writerow([ga.network.quality()])

def plot_ga_compare_routes(file, amount_of_routes, highest_values_only): 

    fig, ax = plt.subplots()

    for r in range(1, amount_of_routes+1):
        with open(f'results/greedyannealing/compare_routes/ga_{r}_routes_{file}.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            values = list(reader)
            values = [float(k) for sublist in values for k in sublist]
            
            if highest_values_only == True: 
                if values[-1] > 5000:
                    iterations = range(len(values))
                    highest_iterations = iterations[-100:]
                    highest_values = values[-100:]
                    ax.plot(highest_iterations, highest_values, label=f'Routes: {r}')
                    name = 'highest_values'
                    
            else: 
            
                if values[-1] > 5000:
                    ax.plot(values, label=f'Routes: {r}')
                else: 
                    ax.plot(values, c="#bfbfbf", label='_nolegend_')
                    name = 'all_values'

    if highest_values_only == True:
        ax.legend(loc='lower left')
    else:
        ax.legend(loc='lower right')
    ax.set_title(f'Greedy Annealing (Tstart: 1000)')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Quality of network')
    fig.set_size_inches(10.5, 7.5)
    fig.savefig(f"results/greedyannealing/compare_routes/compare_routes_{name}_{file}.png")


# ====================== Comparing different temperatures ======================

def greedy_anneal_compare_temps(file, random_network, all_stations, heuristic, iterations=1000, temperature=1000):

    for temp in range(100, temperature+100, 100): 

        ga = GreedyAnnealing(random_network, all_stations, temp, heuristic)

        with open(f'results/greedyannealing/compare_temps/ga_temp{temp}_{file}.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            for i in tqdm(range(iterations), desc=f'Greedy Annealing, temp{temp}:', leave=False): 
                ga.run(1)
                writer.writerow([ga.network.quality()])

def plot_ga_compare_temps(file, temperature): 

    fig, ax = plt.subplots()
    cmap = plt.colormaps["plasma"]

    for temp in range(100, temperature+100, 100):
        with open(f'results/greedyannealing/compare_temps/ga_temp{temp}_{file}.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            values = list(reader)
            values = [float(k) for sublist in values for k in sublist]
            ax.plot(values, label=f'Temp: {temp}', color=cmap(temp/1100))
    
    
    ax.legend(loc='lower right')
    ax.set_title(f'Greedy Annealing: different temperatures')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Quality of network')
    fig.set_size_inches(10.5, 7.5)
    fig.savefig(f"results/greedyannealing/compare_temps/compare_temps_{file}.png")




