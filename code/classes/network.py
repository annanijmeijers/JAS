import copy 

class Network(): 

    def __init__(self, total_tracks, ammount_of_routes):         

        self.total_tracks = total_tracks 
        self.ammount_of_routes = ammount_of_routes
        self.name = 'network'

        #  store the different routes 
        self.routes = []

        # storing all the covered tracks and unique connections 
        self.covered_tracks = None  
        self.unique_tracks  = None 
        self.p = 0 

        # storing the total duration of all routes 
        self.total_duration = 0 
    
    def add_route(self, route_obj):
        """
        IN: Route-object, a list of connections covered by the route 
        Add the route to a list, add the set of covered tracks for this route
        to the total set of covered tracks 
        """

        self.routes.append(route_obj)
                                                      
    
    def get_route(self, r): 
        """
        Returns the Route in the Network with the given number 
        """ 
        return self.routes[r-1]
    
    def replace_route(self, r, replace_route): 
         """
         IN: the number of the Route (int) to delete, and the new Route to insert.

         Replaces a given Route in the Network
         """ 
        
        # loop over all Routes to find the corresponding Route 
         new_routes = copy.deepcopy(self.routes)
         for i in range(len(self.routes)): 
             if self.routes[i].number == r:

                # give the number of the old route to the new route and replace it 
                replace_route.number = self.routes[i].number
                new_routes[i] = replace_route 

         self.routes = new_routes 

    def calculate_network(self):
        """
        Calculate the unique connections used, leveraging the properties of sets.
        This will result in the ammount of connections covered in the network
        """ 
        self.unique_tracks = set()
        self.covered_tracks = set()
        self.total_duration = 0 

        for route in self.routes: 
            self.covered_tracks = self.covered_tracks.union(route.connection_set)
            self.total_duration = self.total_duration + route.duration

        for i,j in self.covered_tracks: 
            if ((i,j) not in self.unique_tracks) and ((j,i) not in self.unique_tracks): 
                self.unique_tracks.add((i,j))
    
            
    def quality(self):
        """"
        Calculates the quality of the network, according to the target function, based on: 
        -fraction of covered tracks
        -ammount of routes 
        -total duration of the network 
        OUT: a value for the target function K 
        """
        
        if not self.routes: 
            print("This Network is empty")
            return 0 

        self.calculate_network()

        self.p = len(self.unique_tracks) / self.total_tracks

        target_function = self.p * 10000 - (self.ammount_of_routes*100 + self.total_duration) 
     
        return target_function 
                 

    def __repr__(self):
        return self.name