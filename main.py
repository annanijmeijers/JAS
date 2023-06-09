import pandas as pd 
import csv 
from code.classes import station 
from code.classes import route 

if __name__ == "__main__":
    
    # load the data 
    df_connections = pd.read_csv('data/ConnectiesHolland.csv')
    df_stations = pd.read_csv('data/StationsHolland.csv')

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name) # naam voor de lijst via __repr__?
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

    
    new_route = route.Route(60, all_stations) # heb dit voor het checken verandert naar 60 min
    new_route.compute_route()
    
    route_names = []
    for sstation in new_route.route: 
        route_names.append(sstation.name)

    print(route_names)
    print(new_route.duration)
    print(new_route.connection_list)

    # unique connections dit in network implementeren toch?
    # EERST alle connection sets mergen voordat deze unique wordt gedaan, anders moet dit 2 keer worden gedaan
    unique_connections = set()
    for i,j in new_route.connection_list:
        if unique_connections:
            if ((i, j) not in unique_connections) and ((j, i) not in unique_connections):
                unique_connections.add((i, j))
        else: 
            unique_connections.add((i, j))
    
    print(unique_connections)
            

# writing the results to a csv-file
with open('rail_network.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')

    writer.writerow(['route', 'station'])
    writer.writerow(['route_1', route_names])
    writer.writerow(['score', 'somescore'])
