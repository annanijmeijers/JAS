import pandas as pd 
from code.classes import station 
from code.classes import route 
from code.classes import network 
from code.algorithms.randomised import RandomRoute
from code.algorithms.greedy import Greedy
from code.run.run import run_random, run_greedy

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

#----------------- EXPERIMENT: RANDOMIZED -----------------
   # run_random(all_stations, df_connections, ammount_of_routes=20,
               #hist_view=True, vis=True)    

#----------------- EXPERIMENT: RANDOMIZED -----------------    
    greedy = Greedy(all_stations, df_connections)
    greedy.run()

    run_greedy(greedy, vis=True)
