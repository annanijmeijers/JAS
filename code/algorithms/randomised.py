import random
from .heuristics.heuristics import choice_heuristic
class RandomRoute(): 

    def __init__(self, route_object, network_object): 
        self.route_object = route_object
        self.network_object = network_object
        self.end_route = False 

    def random_initialise(self):
        """
        IN: Route-object
        Initialises the route by choosing a random Station-object from 
        a list of stations stored in Route
        """
        # choosing the station and adding it to the route
        station = random.choice(self.route_object.list_of_stations)
        self.route_object.add_station(station)

        return 

    def random_connection(self, heuristic): 
        """
        IN: Route-object 
        Checks possible connections for the last station in the route 
        and picks a random new connection and adds it to the route 
        """
        connection_options = self.route_object.check_connection()
        new_connections = choice_heuristic(connection_options, heuristic,
                                           self.route_object, self.network_object)
        next_connection = random.choice(new_connections)

        # only add the connection if it does not surpass the timeframe 
        if connection_options[next_connection] + self.route_object.duration <= self.route_object.timeframe: 
            self.route_object.add_connection(next_connection, connection_options)
        
        else: 
            self.end_route = True 

        return 

    def build_route(self, heuristic='station_based'): 
        """
        IN: Route-object 
        Implements random_initialise to initialise the route and implements 
        random_connection until the duration surpasses the timeframe given to the route
        """
        self.random_initialise()
        while self.route_object.duration < self.route_object.timeframe and self.end_route == False:
            self.random_connection(heuristic)

        return  
