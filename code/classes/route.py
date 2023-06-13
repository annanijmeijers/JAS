from .station import Station 
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

    def add_station(self, station_obj): 
        # get a starting station from dataframe
        # can be random or picked with a specific constraint
        
        self.route.append(station_obj)

    def check_connection(self):
        
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

        return connections
    
    def add_connection(self, connection_key, connections): 
        # increase duration of route and decrease the total timeframe
        self.duration += connections[connection_key]
        self.timeframe -= connections[connection_key]

        stations_list = set(self.list_of_stations)
        for station in self.list_of_stations: # is dit handig via een set? Dit is niet super efficient
            
            # searches for the station object of the connection station
            if station.name == connection_key: 
                self.add_station(station)

    def compute_route(self):
        # compute unique connections
        for i in range(len(self.route)):
            if i < (len(self.route) - 1):
                self.connection_list.add((self.route[i].name, self.route[i+1].name))
