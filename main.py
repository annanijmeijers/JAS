import pandas as pd 
import numpy as np
import random 
import matplotlib.pyplot as plt
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
from code.user_interface.menus import holland_or_national, algorithm_menu, heuristic_menu, railclimber_menu, simulated_annealing_menu, heur_or_beginstation  


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

            # still need to add options here:

            # heur_or_beginstation()

            # heur_or_stat = int(input('You have chosen the Greedy algorithm. Now choose whether you want to pick a heuristic or the way to choose a begin station: '))

            # while heur_or_stat != 0: 

            #     if heur_or_stat == 1: 

            #     if heur_or_stat == 2: 


            heuristic_menu()

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

        # option 3: RandomGreedy
        elif option == 3: 

            heuristic_menu()

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
                
        # option 4: Railclimber
        elif option == 4: 

            railclimber_menu()

            ######## still need to add the right text and choice options #################
            railclimber_choice = int(input('Please enter the number before your choice: '))

            while railclimber_choice != 0: 

                # railclimber_choice 1: blabla
                if railclimber_choice == 1: 

                    rc = stochastic_railclimber(file, random_network, all_stations)

                    break

                # railclimber_choice 2: blabla
                if railclimber_choice == 2: 

                    break   



        elif option == 5: 

            simulated_annealing_menu()

            ######## still need to add the right text and choice options #################
            sim_ann_choice = int(input('Please enter the number before your choice: '))

            while sim_ann_choice != 0: 

                # sim_ann_choice 1: blabla
                if sim_ann_choice == 1: 

                    # run simulated annealing and greedy annealing 
                    sa = simulated_annealing(file, random_network, all_stations)
                    ga = greedy_annealing(file, random_network, all_stations, unique_connections_heuristic)
                    hc = stochastic_railclimber(file, random_network, all_stations)

                    plot_sa_vs_ga_vs_hc(file)


                    break

                # sim_ann_choice 2: blabla
                if sim_ann_choice == 2: 

                    # runs greedy anneal for all numbers of routes in a network 
                    greedy_anneal_compare_routes(file, network_object, all_stations, amount_of_routes, unique_connections_heuristic)

                    # plot the qualities for the different routes, put highest_values_only on True to zoom in in the plot 
                    plot_ga_compare_routes(file, amount_of_routes, highest_values_only=False)
                    break

                # sim_ann_choice 3: blabla
                if sim_ann_choice == 3: 
                    temp = 1000
                    # greedy_anneal_compare_temps(random_network, all_stations, unique_connections_heuristic, 100, temp)
                    plot_ga_compare_temps(file, temp)

                    break 

                # sim_ann_choice 4: blabla
                if sim_ann_choice == 4: 

                    # choice 4 
                    ga = greedy_annealing(file, random_network, all_stations, unique_connections_heuristic)
                    break 

                # sim_ann_choice 5: blabla
                if sim_ann_choice == 5: 

                    # choice 5 
                    break 


        else: 
            print('Invalid choice, please choose again: ')

        algorithm_menu()

        option = int(input('Please enter your algorithm of choice by entering the number: '))

    # if user exits menu print goodbye message
    print('Thankyou for trying our experiments! Have a nice day!')
