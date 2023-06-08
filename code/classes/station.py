import pandas as pd

class Station(): 

    def __init__(self, station_name): # what parameters when calling this object? 
        self.name = station_name
        self.connections = None 
        self.coordinates = None 
        self.passed = False
        self.begin_station = False 
        pass

    
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

        destinations = station_df_left.append(swapped_station).drop('station1', axis=1).reset_index()

        connections = {}
        for index, row in destinations.iterrows():
            connections[row['station2']] = row['distance']

        self.connections = connections

    def set_coordinates(self, coordinates): 
        """ 
        # maybe useful when creating a map? 
        This function sets the coordinates of a station
        """
        self.coordinates = coordinates
        pass 


    def check_passed(self): 
        """
        This function checks if the station 
        has already been passed in a route.
        """
        self.passed = True 
        pass

    def check_begin_station(self): 
        """ 
        This function defines if the station 
        is used as a begin station. If the station 
        is already a begin station in one route, 
        it cannot be used as begin station in another 
        route. 
        """
        self.begin_station = True 
        pass

    def __str__(self): 
        """
        This function helps present the station-object 
        readable. 
        """
        return f'Station: {self.name}, Coords: {self.coordinates}, '\
               f'Passed: {self.passed}, Begin station: {self.check_begin_station}'



# test_station = Station('Amsterdam Sloterdijk')
# test_station.find_connections(df)
# print(test_station.station_name)
# print(test_station.connections)

