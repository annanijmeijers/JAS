import pandas as pd

class Station(): 

    def __init__(self, station_name):
        self.name = station_name
        self.connections = None 
        self.begin_station = False
        self.connections_count = 0

    def find_connections(self, df):
        """
        IN: dataframe 
        OUT: dictionary containing all the destinations, including disitance
        """

        # swap columns of dataframe
        station_mask = df['station1'] == self.name
        station_df_left = df[station_mask]
        station_mask2 = df['station2'] == self.name
        station_df_right = df[station_mask2]

        swapped_station = station_df_right.rename(columns={'station1': 'station2', 'station2': 'station1'})

        destinations = pd.concat([station_df_left, swapped_station]).drop('station1', axis=1).reset_index()

        # create dictionary for the connections
        connections = {}
        for index, row in destinations.iterrows():
            self.connections_count += 1
            connections[row['station2']] = row['distance']

        self.connections = connections


    def is_begin_station(self): 
        """ 
        If called, status of station is set 
        to begin station
        """
        self.begin_station = True 


    def __repr__(self):
        return self.name


