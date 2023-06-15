import random

class RandomRoute(): 

    def __init__(self, route_object): 
        self.route_object = route_object
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

    def random_connection(self): 
        """
        IN: Route-object 
        Checks possible connections for the last station in the route 
        and picks a random new connection and adds it to the route 
        """
        connection_options = self.route_object.check_connection()
        next_connection = random.choice(list(connection_options.keys()))

        # only add the connection if it does not surpass the timeframe 
        if connection_options[next_connection] + self.route_object.duration <= self.route_object.timeframe: 
            self.route_object.add_connection(next_connection, connection_options)
        
        else: 
            self.end_route = True 

        return 

    def build_route(self): 
        """
        IN: Route-object 
        Implements random_initialise to initialise the route and implements 
        random_connection until the duration surpasses the timeframe given to the route
        """
        self.random_initialise()
        while self.route_object.duration < self.route_object.timeframe and self.end_route == False:
            self.random_connection()

        return  
