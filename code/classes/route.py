from .station import Station 
import random
import copy


class Route(): 

    def __init__(self, timeframe, list_of_stations): 
        # needs to contain a variable that keeps track of the route, 
        # and the total duration of the route
        self.list_of_stations = list_of_stations
        self.timeframe = timeframe

        self.duration = 0
        self.route = list()
        self.connection_list = set()

    def initialise_route(self): 
        # get a starting station from dataframe
        # can be random or picked with a specific constraint
        
        starting_station = random.choice(self.list_of_stations)
        self.route.append(starting_station)

    def add_connection(self): 

        # create instance for current station
        current_station = self.route[-1] # chooses the last station in the route station objects

        # choose random connection
        connections = copy.deepcopy(current_station.connections) # gives connections dictionary
        
        # removes previously visited station(s) from connections
        for station in self.route:
            if station.name in connections.keys():
                del connections[station.name]

        # quick fix for empty connections dict
        if connections == {}:
            connections = current_station.connections

        random_connection = random.choice(list(connections.keys())) # picks a random dict key as connection

        # increase duration of route and decrease the total timeframe
        self.duration += connections[random_connection]
        self.timeframe -= connections[random_connection]

        for station in self.list_of_stations: # is dit handig via een set? Dit is niet super efficient
            
            # searches for the station object of the random connection station
            if station.name == random_connection: 
                self.route.append(station)

    def compute_route(self):
        #  makes a route within the timeframe
        self.initialise_route()

        while self.timeframe > 0: # checken of dit niet aan t begin moet
            self.add_connection()

        # compute unique connections
        for i in range(len(self.route)):
            if i < (len(self.route) - 1):
                self.connection_list.add((self.route[i].name, self.route[i+1].name))
