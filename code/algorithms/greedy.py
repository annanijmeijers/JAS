import copy 
import random 
#from code.classes import station 
from code.classes import route 
from code.classes import network 


class Greedy(): 
    """ 
    The Greedy class creates a network in which the best
    possible value to each station in a route is assigned
    one by one. 
    """

    def __init__(self, station_list, connection_list): 
        """ 
        IN: - station_list: list of station objects
            - connection_list: connections DataFrame
        """
        self.station_list = copy.deepcopy(station_list)
        self.connection_list = connection_list
        


    def find_begin_station(self): 
        """ 
        picks begin station from station list with station objects. 
        """
        count_connections = []
        stations = []

        for station in self.station_list: 

            # check if station has already been a begin station 
            if not station.begin_station:
                stations.append(station)
                count_connections.append(station.connections_count)

        # get the index of the station with least connections
        min_index = count_connections.index(min(count_connections))

        min_connections_station = stations[min_index]
        min_connections_station.begin_station = True

        return min_connections_station
    


    def get_next_station(self, route_object, heuristic): 
        """ 
        IN: route object

        Searches in station object for next possible 
        stations returns best possible station object. 

        OUT: station object (next station)
        """

        # this gives a dictionary with connection options 
        connection_options = route_object.check_connection()

        next_station = heuristic(connection_options, self.station_list)
        if not next_station:
            route_object.end_route = True
            return
        
        if (connection_options[next_station.name] + route_object.duration) <= route_object.timeframe: 

            return next_station
        
        else:
            route_object.end_route = True
            return

    def build_route(self, r, heuristic):
        # initialise a route-object and computing the route 
        new_route = route.Route(self.timeframe, self.station_list, r) 
        first_station = self.find_begin_station()

        # add station to current route
        new_route.add_station(first_station)

        # while time limit is not exceeded 
        while new_route.duration <= self.timeframe and not new_route.end_route: 

            next_station = self.get_next_station(new_route, heuristic)

            if not new_route.end_route: 
                #new_route.add_station(next_station)
                new_route.add_connection(next_station.name, new_route.check_connection()) 
        return new_route

    def run(self, heuristic): 
        """ 
        Greedily assigns the station with the highest number of connections 
        to the route. It repeats until the time limit is reached. 
        """
        if len(self.connection_list) == 28:
            amount_of_routes = 7
            self.timeframe = 120
        elif len(self.connection_list) == 89:
            amount_of_routes = 20
            self.timeframe = 180
        
        # initialise a network, give it the total ammount of connections  
        self.rail_net = network.Network(len(self.connection_list), amount_of_routes)

        for r in range(1, amount_of_routes+1): 

            new_route = self.build_route(r, heuristic)
            # send to network how many connections there are
            new_route.compute_covered_connections()
            #print(new_route.route) #CHECKS
            # add the route and the unique connections to the network 
            self.rail_net.add_route(new_route)
            self.rail_net.calculate_network()
        
            # compute unique connections
            if len(self.rail_net.unique_tracks) == self.rail_net.total_tracks:
                self.rail_net.ammount_of_routes = r
                break

        # identify all unique connections in the network 
        self.rail_net.calculate_network()

class RandomGreedy(Greedy):

    def find_begin_station(self):
        """ 
        picks random begin station from station list with station objects. 
        """
        
        begin_station = random.choice(self.station_list)
        begin_station.begin_station = True

        return begin_station                 