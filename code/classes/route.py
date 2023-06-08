from .station import Station 
import random
class Route(): 

    def __init__(self, timeframe, list_of_stations): 
        # needs to contain a variable that keeps track of the route, 
        # and the total duration of the route
        self.route = []
        self.timeframe = timeframe
        self.duration = 0
        self.list_of_stations = list_of_stations

    def initialise_route(self): 
        # get a starting station from dataframe
        # can be random or picked with a specific constraint
        
        starting_station = random.choice(self.list_of_stations)
        self.route.append(starting_station)

    def add_connection(self): 
        # create instance for current station
        current_station = self.route[-1] # chooses the last station in the route station objects

        # choose random connection
        connections = current_station.connections # gives connections dictionary
        random_connection = random.choice(list(connections.keys())) # picks a random dict key as connection

        # increase duration of route and decrease the total timeframe
        self.duration += connections[random_connection]
        self.timeframe -= connections[random_connection]

        for station in self.list_of_stations: # is dit handig via een set?
            if station.name == random_connection: # searches for the station object of the random connection station
                self.route.append(station)

        # wel de keuzes binnen het tijdframe houden 
        '''       
        for connection_name, time in connections.items():
            if (Station(connection_name).passed == False) and (self.timeframe - time > 0):
                self.route.append(connection_name)
                Station(connection_name).passed = True
                self.duration += time
                self.timeframe -= time
         
        # check if the current station is the last station
        if current_station == self.route[-1]:
            pass # doorgeven dat de route klaar is
        '''
    def compute_route(self):
        #  makes a route within the timeframe
        self.initialise_route()

        while self.timeframe > 0: # checken of dit niet aan t begin moet
            self.add_connection()