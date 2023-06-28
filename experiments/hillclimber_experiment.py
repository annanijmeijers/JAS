import csv 
from tqdm import tqdm 
from code.algorithms.hillclimber import StochasticClimber

def stochastic_railclimber(file, random_network, all_stations, iterations=1000):
    """
    Runs Stochastic Hillclimber a given ammount of iterations, dumps the data into a csv file
    """ 

    rc = StochasticClimber(random_network, all_stations)

    with open(f'results/hillclimber/stochastic_railclimber_{file}.csv', 'w', newline='') as f: 
        writer = csv.writer(f, delimiter=',')

        for i in tqdm(range(iterations), desc='StochasticClimber: '): 
            rc.run(1)
            writer.writerow([rc.network.quality()])

    return rc.network

