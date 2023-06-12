import pandas as pd 
import csv 
from code.classes import station 
from code.classes import route 
from code.classes import network 

if __name__ == "__main__":
    
    # load the data 
    df_connections = pd.read_csv('data/ConnectiesHolland.csv')
    df_stations = pd.read_csv('data/StationsHolland.csv')

    # initialising a csv-file to write the results to 
    f = open('rail_network.csv', 'w')
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['route', 'station'])

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __str__?
        
        # storing available connections to each station 
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

    ammount_of_routes = 3
    # initialise a network, give it the total ammount of connections  
    rail_net = network.Network(len(df_connections), ammount_of_routes)

    for r in range(1,ammount_of_routes+1): 

        new_route = route.Route(60, all_stations) # heb dit voor het checken veranderd naar 60 min
        new_route.compute_route()

        # unique connections dit in network implementeren toch?
        # EERST alle connection sets mergen voordat deze unique wordt gedaan, anders moet dit 2 keer worden gedaan
        unique_connections = set()
        for i,j in new_route.connection_list:
            if unique_connections:
                if ((i, j) not in unique_connections) and ((j, i) not in unique_connections):
                    unique_connections.add((i, j))
            else: 
                unique_connections.add((i, j))
        
        # add the route and the unique connections to the network 
        rail_net.add_route(new_route, unique_connections)

        writer.writerow([f'route_{r}', new_route.route])

    rail_net.calculate_unique_connections()
    quality = rail_net.quality()

    writer.writerow(['score', quality])
    f.close()
