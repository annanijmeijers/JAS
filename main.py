import pandas as pd 
from code.classes import station 

if __name__ == "__main__":
    
    # load the data 
    df_connections = pd.read_csv('data/ConnectiesHolland.csv')
    df_stations = pd.read_csv('data/StationsHolland.csv')

    # instantiating a Station object for all stations
    all_stations = []
    for station_name in df_stations['station']:
        new_station = station.Station(station_name)
        new_station.find_connections(df_connections)
        all_stations.append(new_station)

    
