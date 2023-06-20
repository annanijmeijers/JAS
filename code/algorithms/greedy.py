import copy 
import random 
from code.classes import station 
from code.classes import route 
from code.classes import network 

class Greedy(): 
    """ 
    The Greedy class assigns the best possible value 
    to each station one by one. 

    IN: 
    - connection_list 
    - station_list

    OUT: 
    - network

    """

    def __init__(self, station_list, connection_list): 
        """ 
        station_list = list of station objects
        """
        self.station_list = copy.deepcopy(station_list)
        self.connection_list = connection_list
        


    def find_begin_station(self): 
        """ 
        picks begin station from station list with station objects. 

        """
        count_connections = []

        for station in self.station_list: 

            # check if station has already been begin station 
            if not station.begin_station:

                count_connections.append(station.connections_count)

        min_index = count_connections.index(min(count_connections))

        min_connections_station = self.station_list[min_index]
        min_connections_station.begin_station = True

        return min_connections_station
    


    def get_next_station(self, route_object): 
        """ 
        IN: route object
        OUT: station object (next station)

        Searches in station object for next possible 
        stations. 

        """

        count_connections =[]
        stations = []

        # this gives a dictionary with connection options 
        connection_options = route_object.check_connection()

        # for every key in dict
        for key in connection_options.keys(): 

            for station in self.station_list: 

                if key == station.name: 
                   
                    count_connections.append(station.connections_count)
                    stations.append(station)
                    
        max_index = count_connections.index(max(count_connections))

        max_connections_station = stations[max_index]

        if (connection_options[max_connections_station.name] + route_object.duration) <= route_object.timeframe: 

            return max_connections_station
        
        else:
            route_object.end_route = True
            return


    

    def run(self): 

        """ 
        Greedily assigns the station with the highest number of connections 
        to the route. It repeats untill the time limit is reached. 

        """
        amount_of_routes = 7
        timeframe = 120

        # initialise a network, give it the total ammount of connections  
        rail_net = network.Network(len(self.connection_list), amount_of_routes)

        for r in range(1, amount_of_routes+1): 

            # initialise a route-object and computing the route 
            new_route = route.Route(timeframe, self.station_list, r) 
            first_station = self.find_begin_station()

            # add station to current route
            new_route.add_station(first_station)

            # while time limit is not exceeded 
            while new_route.duration <= timeframe and not new_route.end_route: 

                next_station = self.get_next_station(new_route)

                if not new_route.end_route: 
                    #new_route.add_station(next_station)
                    new_route.add_connection(next_station.name, new_route.check_connection()) 


            # send to network how many connections there are
            new_route.compute_covered_connections()
            print(new_route.route)
            # add the route and the unique connections to the network 
            rail_net.add_route(new_route, new_route.connection_set)
            rail_net.calculate_unique_connections()
        
            # compute unique connections
            if len(rail_net.unique_tracks) == rail_net.total_tracks:
                rail_net.ammount_of_routes = r
                break

        # identify all unique connections in the network 
        rail_net.calculate_unique_connections()
        print(rail_net.routes)
        # calculate the quality of the network 
        quality = rail_net.quality()
        print(quality)

