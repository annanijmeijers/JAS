from .route import Route

class Network(): 

    def __init__(self): 

        self.p = None 
        self.t = None 
        self.min = None 

        #  store the different routes 
        self.routes = []
        
        pass 
    
    def total_tracks(sel): 
        """
        Calculate total tracks, given a ... of tracks
        """
        pass 

    def covered_tracks(self): 
        """
        Calculates the fraction of covered tracks: p
        """
        # return covered_tracks / self.total_tracks
        

        pass 

    def quality(self):

        # self.covered_tracks = ...

        # method to calculate the quality of the network using the doelfunctie
        # p = fractie bereden verbindingen --> we moeten dus ergens bijhouden hoeveel verbindingen 
        # we hebben bereden 

        # return quality 
        target_function = self.p * 10000 - (self.t*100 + self.min) 
     
        pass 