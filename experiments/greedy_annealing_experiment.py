import csv 
from tqdm import tqdm 
from code.algorithms.randomised import RandomNet
from code.algorithms.simulatedannealing import GreedyAnnealing
import matplotlib.pyplot as plt 

def greedy_annealing(network_object, all_stations, ammount_of_routes, heuristic, iterations=1000): 

    random_algorithm = RandomNet(network_object, all_stations, ammount_of_routes, route_time=180)
    random_algorithm.run()
    random_network = random_algorithm.network 
    temperature = 1000

    ga = GreedyAnnealing(random_network, all_stations, temperature, heuristic)

    with open('results/greedyannealing/greedyannealing.csv', 'w', newline='') as f: 
        writer = csv.writer(f, delimiter=',')

        for i in tqdm(range(iterations), desc='Greedy Annealing:'): 
            ga.run(1)
            writer.writerow([ga.network.quality()])

    return ga.network.quality()

def greedy_anneal_compare_routes(network_object, all_stations, ammount_of_routes, heuristic, iterations=1000):

    random_algorithm = RandomNet(network_object, all_stations, r, route_time=180)
    random_algorithm.run()
    random_network = random_algorithm.network 

    for r in range(1, ammount_of_routes+1): 

        temperature = 1000
        ga = GreedyAnnealing(random_network, all_stations, temperature, heuristic)

        with open(f'results/greedyannealing/compare_routes/ga_{r}_routes.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            for i in tqdm(range(iterations), desc=f'Greedy Annealing, routes{r}:', leave=False): 
                ga.run(1)
                writer.writerow([ga.network.quality()])

def plot_ga_compare_routes(amount_of_routes): 

    fig, ax = plt.subplots()

    for r in range(1, amount_of_routes+1):
        with open(f'results/greedyannealing/compare_routes/ga_{r}_routes.csv', 'r') as f:
            values = []
            result_reader = csv.reader(f, delimiter=',')
            for row in result_reader: 
                values.append(float(row))

        ax.plot(values, label=f'Routes {r}')

    ax.legend(loc='upper right')
    ax.set_title('Greedy Annealing')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Quality of network')
    fig.savefig(f"results/greedyannealing/compare_routes/compare_routes.png")





