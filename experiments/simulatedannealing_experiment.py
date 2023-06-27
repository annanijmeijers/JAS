import csv 
from tqdm import tqdm 
from code.algorithms.randomised import RandomNet
from code.algorithms.simulatedannealing import SimulatedAnnealing, GreedyAnnealing
import matplotlib.pyplot as plt 

def simulated_annealing(random_network, all_stations, iterations=1000, temperature=1000):
    """
    This function runs the simulated annealing algorithm with a given number iterations
    """
    ga = SimulatedAnnealing(random_network, all_stations, temperature)

    with open('results/simulatedannealing/simulatedannealing.csv', 'w', newline='') as f: 
        writer = csv.writer(f, delimiter=',')

        for i in tqdm(range(iterations), desc='Simulated Annealing:'): 
            ga.run(1)
            writer.writerow([ga.network.quality()])

    return ga.network

def plot_sa_vs_ga_vs_hc(): 
    """
    This function plots the results from simulated annealing, greedy annealing and stochastic hillclimber
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
    
    with open(f'results/hillclimber/stochastic_railclimber.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        values = list(reader)
        values = [float(k) for sublist in values for k in sublist]
        ax.plot(values, label='Stochastic Hillclimber')
            
    ax.legend(loc='lower right')
    ax.set_title('Simulated Annealing versus Greedy Annealing versus HillClimber')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Quality of network')
    fig.set_size_inches(10.5, 7.5)
    fig.savefig(f"results/simulatedannealing/sim_vs_ga_vs_hc.png")


