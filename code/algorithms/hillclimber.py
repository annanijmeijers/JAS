from .randomised import RandomRoute
from ..classes.route import Route 
from tqdm import tqdm 
import copy 
import random

class RailClimber(): 
    """
    This algorithm accepts a filled network, takes a random route from the network and tries to find a 
    better one. It does this for all the routes in the network
    """

    def __init__(self, network_object, all_stations):
        self.network = copy.deepcopy(network_object) 
        self.all_stations = all_stations 
        self.old_score = self.network.quality()
        self.new_score = None
        self.route_to_replace = None 
        self.qualities_for_vis = []

    def replace_and_test(self, r): 
        # get the old route from the Network 
        self.route_to_replace = self.network.get_route(r)

        # create a new random Route 
        new_route = Route(180, self.all_stations) 
        RandomRoute(new_route).build_route()

        # replace the route and calculate the new quality 
        self.network.replace_route(r, new_route)
        self.new_score = self.network.quality()

        # check if the quality is better 
        if self.new_score >= self.old_score:
            self.old_score = self.new_score 
            self.qualities_for_vis.append(self.old_score)

        # put back the old route if the quality is not better or the same  
        else: 
            self.network.replace_route(r, self.route_to_replace)


    def run(self, iterations=100):

        self.qualities_for_vis = []

        # shuffle the iterations to choose the route to change randomly 
        random_list = list(range(1, len(self.network.routes)+1))
        random.shuffle(random_list)
        for r in tqdm(random_list): 

            # try to find a better route 
            for t in tqdm(range(iterations), desc='Tries', leave=False): 

                self.replace_and_test(r)

        return 

class StochasticClimber(RailClimber): 

    def run(self, iterations): 

        self.qualities_for_vis = []

        for i in tqdm(range(iterations)): 

            # choose a random route to change 
            route_to_replace = random.choice(self.network.routes)
            number_of_route = route_to_replace.number

            self.replace_and_test(number_of_route) 
        
            
                
                    
                











    