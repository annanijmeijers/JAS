from .route import Route

class Network(): 

    def __init__(self, dataframe, routes): 

        self.p = None 
        self.routes = routes 
        self.min = None 

        #  store the different routes 
        self.routes = []

        # storing all the covered tracks
        self.tracks = []

        pass 

    def add_route(self):
        pass

    def covered_tracks(self): 
        """
        Calculates the fraction of covered tracks: p
        """
        return len(self.tracks) / len(self.total_tracks) 
        

    def quality(self):

        # self.covered_tracks = ...

        # method to calculate the quality of the network using the doelfunctie
        # p = fractie bereden verbindingen --> we moeten dus ergens bijhouden hoeveel verbindingen 
        # we hebben bereden 


        p = self.covered_tracks

        target_function = p * 10000 - (self.routes*100 + self.min) 
     
        pass 