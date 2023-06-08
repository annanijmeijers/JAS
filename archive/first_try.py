import pandas as pd 

df = pd.read_csv('ConnectiesHolland.csv')
# print(df)

# need to make this object-oriented, w/ name Route? 

class Route(): 
   def __init__(self, dataframe):
       self.route = []
       self.df = dataframe

   def give_destinations(self, station): 
        """
        Takes the name of a station and and a general dataframe, returns a dataframe containing all 
        the destionations, including distance 
        """
        station_mask = self.df['station1'] == station
        station_df_left = self.df[station_mask]
        station_mask2 = self.df['station2'] == station
        station_df_right = self.df[station_mask2]

        swapped_station = self.df.rename(columns={'station1': 'station2', 'station2':'station1'})
    
        destinations = station_df_left.append(swapped_station).drop('station1', axis=1).reset_index()

        return destinations  

   def determine_best_direction(self, station, dataframe, passed_stations, distance_travelled, max_travel_time):
        """
        Takes a station, a dataframe with all possible connections (not only for that station), and a list of passed stations to
        determine the next station (direction). Constraints for this directions are the passed stations 
        and the maximum travel time
        """
        destinations = give_destinations(station, dataframe)
        for i in range(len(destinations)): 
            if destinations['station2'][i] not in passed_stations:
                if distance_travelled + destinations['distance'][i] <= max_travel_time: 
                    direction = destinations['station2'][i]
                    passed_stations.append(direction)
                    return direction


   def create_route(station1, station2, dataframe):
        
        # Needs to recursively implement determine_best_direction to create a route

        pass


destinations = give_destinations('Amsterdam Sloterdijk', df)
print(destinations)

new_direction = determine_best_direction('Amsterdam Sloterdijk', df, ['Zaandam'], 10, 120)
print(new_direction)