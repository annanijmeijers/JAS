import pandas as pd 
from code.classes import station 
from code.classes import route 
from code.classes import network 
from code.algorithms.randomised import RandomRoute
from code.algorithms.greedy import Greedy
from code.run.run import run_random

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
    # ammount of routes per network 
    # ammount_of_routes = 7

# ------------------ NATIONAL ---------------------------------
    df_connections = pd.read_csv('data/ConnectiesNationaal.csv')
    df_stations = pd.read_csv('data/StationsNationaal.csv')

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
        # storing available connections to each station 
        new_station.find_connections(df_connections)
        all_stations.append(new_station)
    # ammount of routes per network 
    ammount_of_routes = 20
#----------------- EXPERIMENT: RANDOMIZED -----------------


    # initialising parameters for experiment 
    runs = 10000
    k_values = []
    best_k = 0 
    best_network = None 

    # ammount of routes per network 
    ammount_of_routes = 20

    for t in tqdm(range(runs)):

        # initialise a network, give it the total ammount of connections  
        rail_net = network.Network(len(df_connections), ammount_of_routes)

        for r in range(1,ammount_of_routes+1): 

            # initialise a route-object and computing the route 
            new_route = route.Route(180, all_stations, r) 
            RandomRoute(new_route).build_route()
            new_route.compute_covered_connections()
            
            # add the route and the unique connections to the network 
            rail_net.add_route(new_route, new_route.connection_set)

            if len(rail_net.unique_tracks) == rail_net.total_tracks:
                rail_net.ammount_of_routes = r
                break

        # identify all unique connections in the network 
        rail_net.calculate_unique_connections()

        # calculate the quality of the network 
        quality = rail_net.quality()

        k_values.append(quality)

        # save the best k and the corresponding Network instance 
        if quality > best_k: 
            best_k = quality 
            best_network = copy.deepcopy(rail_net)
    print(f"With {len(best_network.routes)} route(s) the best K is: {best_k}")


#----------------- EXPERIMENT VISUALISATION -----------------
plt.hist(k_values, bins = 1000)
plt.xlabel('Value for K')
plt.ylabel('Ammount')
plt.title('Values for K using the Randomized algorithm')
plt.savefig('code/visualisation/plots/Histogram.png') # maar 1 keer gebruiken denk ik?
plt.show

#----------------- NETWORK VISUALISATION -----------------

# ------------------- HOLLAND ----------------------------
# Create list with stations
# csv_file = 'data/StationsHolland.csv' 
# station_list_holland = extract_stations(csv_file)

# # Create list with connections
# csv_file_connections = 'data/ConnectiesHolland.csv'
# connections_holland = read_connections(csv_file_connections)

# visualise(station_list_holland, connections_holland, best_network)

# ------------------- NATIONAL ----------------------------


# Create list with stations
csv_file = 'data/StationsNationaal.csv' 
station_list_national = extract_stations(csv_file)

# Create list with connections
csv_file_connections = 'data/ConnectiesNationaal.csv'
connections_national = read_connections(csv_file_connections)

visualise(station_list_national, connections_national, best_network)

   # run_random(all_stations, df_connections, ammount_of_routes=20,
               #hist_view=True, vis=True)    
    
#----------------- EXPERIMENT: GREEDY ----------------------
    greedy = Greedy(all_stations, df_connections)
    greedy.run()
