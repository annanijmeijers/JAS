class Station(): 

    def __init__(self, station_name): # what parameters when calling this object? 
        self.station_name = station_name
        self.coordinates = None 
        self.check_passed = False
        self.check_begin_station = False 

        pass

    def set_coordinates(self, coordinates): 
        """ 
        # maybe useful when creating a map? 
        This function sets the coordinates of a station
        """
        self.coordinates = coordinates

    def connections(self, connections):

        """ 
        # determine what form 'connections' will be of
        # maybe dictionary? Then we would have to write something 
        # that will transform the connection list into a dictionary! 

        This function takes connections and searches for 
        the connections of the current station (self.station) 
        it then creates a dictionary of all 
        connections of this station with the corresponding 
        connection durations. The connected stations are 
        the keys and the duration of the connection to that 
        station is the value. 
        """
        # retrieve the information of this station from 
        # connections
        self.connections = connections
        self.conncections_durations = {}


    	# this is just a test piece of code --> not right
        self.conncections_durations[self.station_name] = self.connections[self.station_name]
        pass 

    def check_passed(self): 
        """
        This function checks if the station 
        has already been passed in a route.
        """
        self.passed = True 

    def check_begin_station(self): 
        """ 
        This function defines if the station 
        is used as a begin station. If the station 
        is already a begin station in one route, 
        it cannot be used as begin station in another 
        route. 
        """
        self.check_begin_station = True 


    def __str__(self): 
        """
        This function helps present the station-object 
        readable. 
        """
        return f'Station: {self.station_name}, Coords: {self.coordinates}, '\
               f'Passed: {self.passed}, Begin station: {self.check_begin_station}'
