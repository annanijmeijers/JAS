from .route import Route

class Network(): 

    def __init__(self):         

        #  store the different routes 
        self.routes = []

        # storing all the covered tracks
        self.covered_tracks = set()

        # storing the total duration of all routes 
        self.total_duration = None 
    
        self.total_tracks = None 

        self.route_number = None 

    def add_route(self, route_list, route_tracks, route_duration):
        """
        Add the route to a list, add the set of covered tracks for this route
        to the total set of covered tracks 
        """

        self.route.append(route_list)
        self.covered_tracks = self.covered_tracks + set(route_tracks)
        self.total_duration = self.total_duration + route_duration


    # def covered_tracks(self): 
    #     """
    #     Calculates the fraction of covered tracks: p
    #     """
    #     return len(self.total_tracks) / len(self.total_tracks) 
        

    def quality(self):
        """"
        Calculates the quality of the network, according to the target function, based on: 
        -fraction of covered tracks
        -ammount of routes 
        -total duration of the network 
        """

        p = len(self.covered_tracks) / len(self.total_tracks)

        target_function = p * 10000 - (self.route_number*100 + self.total_duration) 
     
        return target_function 