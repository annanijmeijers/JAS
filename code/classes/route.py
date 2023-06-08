from .station import Station 
import pandas
class Route(): 

    def __init__(self, timeframe, df): 
        # needs to contain a variable that keeps track of the route, 
        # and the total duration of the route
        self.route = []
        self.timeframe = timeframe
        self.duration = 0
        self.df = df

    def initialise_route(self): 
        # get a starting station from dataframe
        # can be random or picked with a specific constraint
        
        starting_station = Station(self.df["station1"].sample()) 
        self.route.append(starting_station)

    def add_connection(self): 
        # create instance for current station
        current_station = self.route[-1]

        # check possible connections choose first available one
        connections = Station(current_station).connections
        for connection_name, time in connections.items():
            if (Station(connection_name).passed == False) and (self.timeframe - time > 0):
                self.route.append(connection_name)
                Station(connection_name).passed = True
                self.duration += time
                self.timeframe -= time
        
        # check if the current station is the last station
        if current_station == self.route[-1]:
            pass # doorgeven dat de route klaar is

    def route(self):
        #  makes a route within the timeframe
        if self.route == []:
            self.initialise_route()

        else:
            if self.timeframe > 0: # checken of dit niet aan t begin moet
                self.add_connection()