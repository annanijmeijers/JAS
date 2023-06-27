import csv 
from tqdm import tqdm 
from code.algorithms.randomised import RandomNet
from code.algorithms.hillclimber import RailClimber, StochasticClimber
import matplotlib.pyplot as plt 

def stochastic_railclimber(random_network, all_stations, iterations=1000): 

    rc = StochasticClimber(random_network, all_stations)

    with open('results/hillclimber/stochastic_railclimber.csv', 'w', newline='') as f: 
        writer = csv.writer(f, delimiter=',')

        for i in tqdm(range(iterations), desc='StochasticClimber: '): 
            rc.run(1)
            writer.writerow([rc.network.quality()])

    return rc.network

