import pandas as pd

class Station(): 

    def __init__(self, station_name): # what parameters when calling this object? 
        self.name = station_name
        self.connections = None 

    def find_connections(self, df):
        """
        Takes the name of a station and a general dataframe, returns a dictionary containing all
        the destinations, including distance
        """
        station_mask = df['station1'] == self.name
        station_df_left = df[station_mask]
        station_mask2 = df['station2'] == self.name
        station_df_right = df[station_mask2]

        swapped_station = station_df_right.rename(columns={'station1': 'station2', 'station2': 'station1'})

        destinations = pd.concat([station_df_left, swapped_station]).drop('station1', axis=1).reset_index()

        connections = {}
        for index, row in destinations.iterrows():
            connections[row['station2']] = row['distance']

        self.connections = connections

    def __repr__(self):
        return self.name


