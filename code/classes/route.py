import copy
from code.algorithms.randomised import RandomRoute 

class Route(): 

    def __init__(self, timeframe, list_of_stations, number=99): 
        self.list_of_stations = list_of_stations
        self.timeframe = timeframe
        self.number = number 

        self.duration = 0
        self.route = list()
        self.connection_set = set()
        self.end_route = False

    def add_station(self, station_obj): 
        """
        IN: - station_obj: Station-object
        This method appends a Station-object to the route list.
        """
        self.route.append(station_obj)

    def check_connection(self):
        """
        This method checks the different amount of connections
        for the last Station-object in the self.route list.
        If a connection station is inside the self.route list
        this station will be removed from the connections.
        The method returns the connections dictionary of that
        list.
        OUT: - connections: Dictionary object that contains the destinations
        """
        current_station = self.route[-1] 
        connections = copy.deepcopy(current_station.connections)
        
        for station in self.route:
            if station.name in connections.keys():
                del connections[station.name]

        return connections
    
    def add_connection(self, connection_key, connections): 
        """
        IN: - connection_key: String value that corresponds to a connection key
            - connections: Dictionary object that contains the destinations
        This method increases the duration of the route based on the travel
        time for the specific connection and it appends the connecting Station
        to the route.
        """
        self.duration += connections[connection_key]
        
        for station in self.list_of_stations:            
            if station.name == connection_key: 
                self.add_station(station)

    def compute_covered_connections(self):
        """
        This method adds connection tuples to the self.connection_set.
        """
        for i in range(len(self.route)):
            if i < (len(self.route) - 1):
                self.connection_set.add((self.route[i].name, self.route[i+1].name))

    def delete_station(self, station_name): 
        """
        IN: name of a station (string)
        Deletes a station and any stations that follow in the route 
        """

        # finding the station in the route-list
        for i in range(len(self.route)): 
            if self.route[i].name == station_name:

                # make a copy of the route until (not including) the station to delete
                new_route = copy.deepcopy(self.route[:i])
        
        # set the route to be the copied route 
        self.route = new_route


    def __repr__(self): 
        return str(self.number)