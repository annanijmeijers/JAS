from .route import Station 

class Route(): 

    def __init__(self, timeframe): 

        # needs to contain a variable that keeps track of the route, 
        # and the total duration of the route
        self.route = []
        self.timeframe = timeframe
        self.duration = 0

        pass 

    def initialise_route(self): 

        # get a starting station from dataframe
        # can be random or picked with a specific constraint
        if self.route == []:
            starting_station = Station() # 
            # self.route.append() starting station name

        pass

    def add_connection(self): 

        # check possible connections choose first available one
        connections = Station(self.route[-1]).connections
        for connection_name, time in connections.items():
            if (Station(connection_name).passed == False) and (self.timeframe - time > 0):
                self.route.append(connection_name)
                Station(connection_name).passed = True
        pass 
