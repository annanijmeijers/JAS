import pandas as pd 
from code.classes import station 
from code.classes import route 
from code.classes import network 
from code.visualisation.visualisation import Visualisation
from code.algorithms.randomised import RandomRoute, RandomNet
from code.algorithms.greedy import Greedy, RandomGreedy
from experiments.greedyannealing_experiment import greedy_annealing, greedy_anneal_compare_routes, plot_ga_compare_routes, plot_ga_compare_temps, greedy_anneal_compare_temps
from experiments.simulatedannealing_experiment import simulated_annealing, plot_sa_vs_ga_vs_hc
from experiments.hillclimber_experiment import stochastic_railclimber
from experiments.greedy.greedy_experiment import greedy, random_greedy, random_greedy_graph, greedy_vis
from experiments.random.random_experiment import random_net, random_graph, random_vis
from code.algorithms.heuristics.heuristics import max_connections_heuristic, unique_connections_heuristic, distance_based_heuristic

if __name__ == "__main__":
    
#----------------- LOADING THE DATA -----------------

    file = input("Which file do you want Holland or Nationaal? ")
    if file == 'Holland':
        df_connections = pd.read_csv('data/ConnectiesHolland.csv')
        df_stations = pd.read_csv('data/StationsHolland.csv')  
        amount_of_connections = 28
        amount_of_routes = 7
        route_time = 120 


    elif file == 'Nationaal':
        df_connections = pd.read_csv('data/ConnectiesNationaal.csv')
        df_stations = pd.read_csv('data/StationsNationaal.csv')
        amount_of_connections = 89
        amount_of_routes = 20
        route_time = 180

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
        # storing available connections to each station 
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

    # empty network object
    network_object = network.Network(amount_of_connections, amount_of_routes)

    # initialising a randomly filled network for iterative algorithms later 
    random_algorithm = RandomNet(network_object, all_stations, amount_of_routes, route_time)
    random_algorithm.run()
    random_network = random_algorithm.network 

# ---------------- PROVIDE MENU CHOICES ------------------------

def menu(): 
    """ 
    Prints a menu of algorithm options from which 
    the user can choose which experiment they would 
    like to run. 
    """
    print('___________ MENU __________')
    print('[1] Randomised')
    print('[2] Greedy')
    print('[3] RandomGreedy')
    print('[4] Railclimber')
    print('[5] Simulated Annealing')
    print('[0] Exit Menu')


def heuristic_menu(): 
    """ 
    Prints a menu of heuristic options from which 
    the user can choose which experiment they would 
    like to run.
    """ 
    print('The options are sorted from the highest score to the lowest score')
    print('___________ MENU ____________________')
    print('[1] Unique Connections Heuristic')
    print('[2] Maximum Connections Heuristic')
    print('[3] Closest Distance Based Heuristic')
    print('[0] Exit Heuristic Menu')




    
def railclimber_menu(): 
    """ 
    Prints a menu of options from which 
    the user can choose which version of the 
    experiment they would like to run.
    """
    print('___________ MENU __________')
    print('[1] option 1')
    print('[2] option 2')
    print('[0] Exit Menu')




def simulated_annealing_menu(): 
    """ 
    Prints a menu of options from which 
    the user can choose which version of the 
    experiment they would like to run.
    """
    print('___________ MENU __________')
    print('[1] Normal Simulated Annealing')
    print('[2] option 2')
    print('[3] option 3')
    print('[0] Exit Menu')



menu()

option = int(input('Please enter your algorithm of choice by entering the number before the algorithm: '))
print('')


while option != 0: 

    # option 1: Random 
    if option == 1: 

        random_net(network_object, all_stations, amount_of_routes) 
        random_graph()
        random_vis(file)  

    # option 2: Greedy  
    elif option == 2: 

        heuristic_menu()

        heuristic_option = int(input('Please enter your heuristic of choice by entering the number before the heuristic: '))

        while heuristic_option != 0: 

            # option 1: unique_connections_heuristic
            if heuristic_option == 1: 

                greedy(all_stations, network_object, unique_connections_heuristic)
                greedy_vis(file, unique_connections_heuristic)
                break 

            # option 2: max_connections_heuristic
            if heuristic_option == 2: 

                greedy(all_stations, network_object, max_connections_heuristic)
                greedy_vis(file, max_connections_heuristic)
                break

            # option 3: distance_based_heuristic
            if heuristic_option == 3: 

                greedy(all_stations, network_object, distance_based_heuristic)
                greedy_vis(file, distance_based_heuristic)
                break

    # option 3: RandomGreedy
    elif option == 3: 

        heuristic_menu()

        heuristic_option = int(input('Please enter your heuristic of choice by entering the number before the heuristic: '))

        while heuristic_option != 0: 

            # option 1: unique_connections_heuristic
            if heuristic_option == 1: 
                # run RandomGreedy 
                random_greedy(network_object, all_stations, unique_connections_heuristic)
                random_greedy_graph()
                greedy_vis(file, random=True)
                break 

            # option 2: max_connections_heuristic
            if heuristic_option == 2: 
                # run RandomGreedy 
                random_greedy(network_object, all_stations, max_connections_heuristic)
                random_greedy_graph()
                greedy_vis(file, random=True)
                break

            # option 3: distance_based_heuristic
            if heuristic_option == 3: 

                # run RandomGreedy 
                random_greedy(network_object, all_stations, distance_based_heuristic)
                random_greedy_graph()
                greedy_vis(file, random=True)
                break
            
    # option 4: Railclimber
    elif option == 4: 

        railclimber_menu()

        railclimber_choice = int(input('Please enter the number before your choice: '))

        while railclimber_choice != 0: 

            if railclimber_choice == 1: 

                rc = stochastic_railclimber(random_network, all_stations)

                break

            if railclimber_choice == 2: 

                break



    elif option == 5: 

        simulated_annealing_menu()

        sim_ann_choice = int(input('Please enter the number before your choice: '))

        while sim_ann_choice != 0: 

            if sim_ann_choice == 1: 

                # run simulated annealing and greedy annealing 
                sa = simulated_annealing(random_network, all_stations)
                ga = greedy_annealing(random_network, all_stations, unique_connections_heuristic)
                hc = stochastic_railclimber(random_network, all_stations)

                plot_sa_vs_ga_vs_hc()


                break

            if sim_ann_choice == 2: 

                # runs greedy anneal for all numbers of routes in a network 
                greedy_anneal_compare_routes(network_object, all_stations, amount_of_routes, unique_connections_heuristic)

                # plot the qualities for the different routes, put highest_values_only on True to zoom in in the plot 
                plot_ga_compare_routes(amount_of_routes, highest_values_only=False)
                break

            if sim_ann_choice == 3: 
                temp = 1000
                greedy_anneal_compare_temps(random_network, all_stations, unique_connections_heuristic, 100, temp)
                plot_ga_compare_temps(temp)

                break 
    else: 
        print('Invalid choice, please choose again: ')

    menu()
    option = int(input('Please enter your algorithm of choice by entering the number before the algorithm: '))

print('Thankyou for trying our experiments! Have a nice day!')

