import csv 
from tqdm import tqdm 
from code.algorithms.randomised import RandomNet
from code.algorithms.simulatedannealing import SimulatedAnnealing, GreedyAnnealing
import matplotlib.pyplot as plt 

def simulated_annealing(network_object, all_stations, ammount_of_routes, heuristic, iterations=1000, plot=True):
    """
    This function runs the simulated annealing algorithm with a given number iterations
    """

    random_algorithm = RandomNet(network_object, all_stations, ammount_of_routes, route_time=180)
    random_algorithm.run()
    random_network = random_algorithm.network 
    temperature = 1000

    ga = SimulatedAnnealing(random_network, all_stations, temperature)

    with open('results/simulatedannealing/simulatedannealing.csv', 'w', newline='') as f: 
        writer = csv.writer(f, delimiter=',')

        for i in tqdm(range(iterations), desc='Simulated Annealing:'): 
            ga.run(1)
            writer.writerow([ga.network.quality()])

    return ga.network

def plot_sa_vs_ga(): 
    """
    This function plots the results from simulated annealing and greedy annealing 
    to compare
    """

    fig, ax = plt.subplots()

    with open(f'results/simulatedannealing/simulatedannealing.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        values = list(reader)
        values = [float(k) for sublist in values for k in sublist]
        ax.plot(values, label='Simulated Annealing')

    with open(f'results/greedyannealing/greedyannealing.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        values = list(reader)
        values = [float(k) for sublist in values for k in sublist]
        ax.plot(values, label='Greedy Annealing')
            
    ax.legend(loc='lower right')
    ax.set_title('Simulated Annealing versus Greedy Annealing (Tstart=1000)')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Quality of network')
    fig.set_size_inches(10.5, 7.5)
    fig.savefig(f"results/simulatedannealing/sim_vs_ga.png")


