import random
import copy 
from ..classes.network import Network
from ..classes.route import Route 

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

        # end the route if there are no connection options left 
        if not connection_options:
            self.end_route = True 
            return 
        
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

class RandomNet(): 

    def __init__(self, network_obj, all_stations, ammount_of_routes=20, route_time=180): 

        self.all_stations = all_stations
        self.ammount_of_routes = ammount_of_routes
        self.route_time = route_time
        self.rail_net = copy.deepcopy(network_obj) 
        self.routes = []
        self.name = 'Random'
    
    def run(self):

        for r in range(1, self.ammount_of_routes+1): 

            # initialise a Route-object and build it  
            new_route = Route(self.route_time, self.all_stations, r) 
            RandomRoute(new_route).build_route()
            new_route.compute_covered_connections()
            
            # add the route and the unique connections to the network 
            self.rail_net.add_route(new_route)

            # append the route to the routes list
            self.routes.append(new_route)

            self.rail_net.calculate_network()
        
            if len(self.rail_net.unique_tracks) == self.rail_net.total_tracks:
                self.rail_net.ammount_of_routes = r
                break

        # identify all unique connections in the network 
        self.rail_net.calculate_network()

        self.random_network = self.rail_net
    
    def return_network(self): 
        return self.rail_net


    def __repr__(self):
        return self.name
