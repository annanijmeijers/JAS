import csv 
from tqdm import tqdm 
from code.algorithms.simulatedannealing import SimulatedAnnealing
import matplotlib.pyplot as plt 

def simulated_annealing(file, random_network, all_stations, iterations=1000, temperature=1000):
    """
    This function runs the simulated annealing algorithm with a given number iterations, dumps the data 
    into a csv-file
    """
    ga = SimulatedAnnealing(random_network, all_stations, temperature)

    with open(f'results/simulatedannealing/simulatedannealing_{file}.csv', 'w', newline='') as f: 
        writer = csv.writer(f, delimiter=',')

        for i in tqdm(range(iterations), desc='Simulated Annealing:'): 
            ga.run(1)
            writer.writerow([ga.network.quality()])

    return ga.network

def plot_sa_vs_ga_vs_hc(file): 
    """
    Reads the csv data from Stochastic Hillclimber, SimulatedAnnealing, 
    and GreedyAnnealing and plots the results to compare
    """

    fig, ax = plt.subplots()

    with open(f'results/simulatedannealing/simulatedannealing_{file}.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        values = list(reader)
        values = [float(k) for sublist in values for k in sublist]
        ax.plot(values, label='Simulated Annealing')

    with open(f'results/greedyannealing/greedyannealing_{file}.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        values = list(reader)
        values = [float(k) for sublist in values for k in sublist]
        ax.plot(values, label='Greedy Annealing')
    
    with open(f'results/hillclimber/stochastic_railclimber_{file}.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        values = list(reader)
        values = [float(k) for sublist in values for k in sublist]
        ax.plot(values, label='Stochastic Hillclimber')
            
    ax.legend(loc='lower right')
    ax.set_title('Simulated Annealing versus Greedy Annealing versus HillClimber')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Quality of network')
    fig.set_size_inches(10.5, 7.5)
    fig.savefig(f"results/simulatedannealing/sim_vs_ga_vs_hc_{file}.png")


