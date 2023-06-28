import pandas as pd 
from code.classes import station 
from code.classes import network 
from visualisation.visualisation import Visualisation
from code.algorithms.randomised import RandomNet
from experiments.greedyannealing_experiment import greedy_annealing, greedy_anneal_compare_routes, plot_ga_compare_routes, plot_ga_compare_temps, greedy_anneal_compare_temps, many_greedy_annealing
from experiments.simulatedannealing_experiment import simulated_annealing, plot_sa_vs_ga_vs_hc
from experiments.hillclimber_experiment import stochastic_railclimber
from experiments.greedy.greedy_experiment import greedy, random_greedy, random_greedy_graph, greedy_vis, heuristic_differences
from experiments.random.random_experiment import random_net, random_graph, random_vis
from code.algorithms.heuristics.heuristics import max_connections_heuristic, unique_connections_heuristic, distance_based_heuristic
from code.user_interface.menus import holland_or_national, algorithm_menu, greedy_menu, random_greedy_menu, railclimber_menu, simulated_annealing_menu


if __name__ == "__main__":

    # present with menu with all options
    print('Welcome to our RailNL Case!')
    print('Please enter which file you like to use.')
    holland_or_national()

    # determine which file the user wants to use
    file = int(input('Holland or National: '))

    while file != 0: 

        # file 1: Holland 
        if file == 1:
                df_connections = pd.read_csv('data/ConnectiesHolland.csv')
                df_stations = pd.read_csv('data/StationsHolland.csv')  
                amount_of_connections = 28
                amount_of_routes = 7
                route_time = 120 
                file = 'Holland'
                break 

        # file 2: National 
        elif file == 2:
            df_connections = pd.read_csv('data/ConnectiesNationaal.csv')
            df_stations = pd.read_csv('data/StationsNationaal.csv')
            amount_of_connections = 89
            amount_of_routes = 20
            route_time = 180
            file = 'Nationaal'
            break

        else: 
            print('Invalid choice, please choose again: ') 

        holland_or_national()
        file = int(input('Holland or National: '))

    # instantiating a Station object for all stations
    all_stations = []

    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
        # storing available connections to each station 
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

    # create empty network object
    network_object = network.Network(amount_of_connections, amount_of_routes)

    # initialising a randomly filled network for iterative algorithms later 
    random_algorithm = RandomNet(network_object, all_stations, amount_of_routes, route_time)
    random_algorithm.run()
    random_network = random_algorithm.network 

    # present user with menu of algorithms
    algorithm_menu()
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
            greedy_menu()
            heuristic_option = int(input('Please enter the number of your heuristic of choice: '))

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

                 # option 3: distance_based_heuristic
                if heuristic_option == 4: 
                    heuristic_differences(file)
                    break

                else:
                    print('Invalid choice, redirecting to algorithm menu')
                    break

        # option 3: RandomGreedy
        elif option == 3: 
            random_greedy_menu()
            heuristic_option = int(input('Please enter the number of your heuristic of choice: '))

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

                else:
                    print('Invalid choice, redirecting to algorithm menu')
                    break

        # option 4: Railclimber
        elif option == 4: 
            railclimber_menu()
            railclimber_choice = int(input('Please enter the number before your choice: '))

            while railclimber_choice != 0: 

                # railclimber_choice 1: stochastic railclimber
                if railclimber_choice == 1: 
                    rc = stochastic_railclimber(file, random_network, all_stations)
                    break 

                else:
                    print('Invalid choice, redirecting to algorithm menu')
                    break

        elif option == 5: 

            simulated_annealing_menu()

            sim_ann_choice = int(input('Please enter the number before your choice: '))

            while sim_ann_choice != 0: 
             
                if sim_ann_choice == 1: 

                    # run simulated annealing and greedy annealing 
                    sa = simulated_annealing(file, random_network, all_stations)
                    ga = greedy_annealing(file, random_network, all_stations, unique_connections_heuristic)
                    hc = stochastic_railclimber(file, random_network, all_stations)

                    plot_sa_vs_ga_vs_hc(file)
                    break

                if sim_ann_choice == 2: 

                    # runs greedy anneal for all numbers of routes in a network 
                    ga = greedy_anneal_compare_routes(file, network_object, all_stations, amount_of_routes, unique_connections_heuristic)
                    
                    # visualize best network 
                    best_network_for_vis = ga.network
                    vis = Visualisation()
                    vis.extract_data(f'data/Stations{file}.csv', f'data/Connecties{file}.csv')
                    vis.visualise(best_network_for_vis, title=f'GreedyAnnealing (routes_{len(best_network_for_vis.routes)}, quality_{best_network_for_vis.quality()})')

                    # plot the qualities for the different routes, put highest_values_only on True to zoom in in the plot 
                    plot_ga_compare_routes(file, amount_of_routes, highest_values_only=True)
                    break

                if sim_ann_choice == 3: 

                    # experiment to compare different starting temperatures 
                    temp = 1000
                    greedy_anneal_compare_temps(file, random_network, all_stations, unique_connections_heuristic)
                    plot_ga_compare_temps(file, temp)
                    break 

                if sim_ann_choice == 4: 

                    # one run of greedy annealing  
                    ga = greedy_annealing(file, random_network, all_stations, unique_connections_heuristic)
                    break 

                if sim_ann_choice == 5: 

                    # many tries to reach the theoretical optimum, using greedy annealing
                    ga = many_greedy_annealing(file, network_object, all_stations, unique_connections_heuristic, 50, route_time, 9)
                    best_network_for_vis = ga.network

                    vis = Visualisation()
                    vis.extract_data(f'data/Stations{file}.csv', f'data/Connecties{file}.csv')
                    vis.visualise(best_network_for_vis, title=f'GreedyAnnealing (routes_{len(best_network_for_vis.routes)}, quality_{best_network_for_vis.quality()})')
                    break 

                else:
                    print('Invalid choice, redirecting to algorithm menu')
                    break


        else: 
            print('Invalid choice, please choose again: ')

        algorithm_menu()
        option = int(input('Please enter your algorithm of choice by entering the number: '))

    # if user exits menu print goodbye message
    print('Thankyou for trying our experiments! Have a nice day!')
