import pandas as pd 
from code.classes import station 
from code.classes import route 
from code.classes import network 
from code.visualisation.visualisation import Visualisation
from code.algorithms.randomised import RandomRoute
from code.algorithms.greedy import Greedy, RandomGreedy
from code.run.run import run_random, run_greedy
from code.algorithms.heuristics.heuristics import max_connections_heuristic, unique_connections_heuristic

if __name__ == "__main__":
    
#----------------- LOADING THE DATA -----------------

# ------------------- HOLLAND ------------------------
    # df_connections = pd.read_csv('data/ConnectiesHolland.csv')
    # df_stations = pd.read_csv('data/StationsHolland.csv')

    # # instantiating a Station object for all stations
    # all_stations = []
    # for station_name in df_stations['station']:
    #     new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
    #     # storing available connections to each station 
    #     new_station.find_connections(df_connections)
    #     all_stations.append(new_station)

# ------------------ NATIONAL ---------------------------------
    file = input("Which file do you want Holland or Nationaal? ")
    if file == 'Holland':
        df_connections = pd.read_csv('data/ConnectiesHolland.csv')
        df_stations = pd.read_csv('data/StationsHolland.csv')  

    elif file == 'Nationaal':
        df_connections = pd.read_csv('data/ConnectiesNationaal.csv')
        df_stations = pd.read_csv('data/StationsNationaal.csv')

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
        # storing available connections to each station 
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

    # empty network object
    network_object = network.Network(len(df_connections), 20)
#----------------- EXPERIMENT: RANDOMIZED -----------------
    random = input("Do you want to run the Random algorithm (y/n)? ")
    if random == 'y':

        run_random(network_object, all_stations, df_connections, ammount_of_routes=20,
               hist_view=True, vis=True)    

#----------------- EXPERIMENT: GREEDY ---------------------
    greedy = input("Do you want to run the Greedy algorithm (y/n)? ")
    if greedy == 'y':
        greedy = Greedy(all_stations, df_connections)
        greedy.run(unique_connections_heuristic)
        run_greedy(greedy, vis=True, iterations=1)

#----------------- EXPERIMENT: GREEDY ---------------------    
    random_greedy = input("Do you want to run the RandomGreedy algorithm (y/n)?")
    if random_greedy == 'y':
        random_greedy = RandomGreedy(all_stations, df_connections)
        random_greedy.run(unique_connections_heuristic)
        run_greedy(random_greedy, vis=True)
