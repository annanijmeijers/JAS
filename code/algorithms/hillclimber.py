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
        self.all_stations = all_stations 
        self.network = copy.deepcopy(network_object) 
        

    def run(self, tries_per_route=100):

        # shuffle the iterations to choose the route to change randomly 
        random_list = list(range(1, len(self.network.routes)+1))
        random.shuffle(random_list)
        for r in tqdm(random_list): 

            best_quality = self.network.quality()

            # try to find a better route 
            for t in tqdm(range(tries_per_route), desc='Tries', leave=False): 

                # get the old route from the Network 
                old_route = self.network.get_route(r)

                # create a new random Route 
                new_route = Route(180, self.all_stations) 
                RandomRoute(new_route).build_route()

                # replace the route and calculate the new quality 
                self.network.replace_route(r, new_route)
                new_quality = self.network.quality()

                # check if the quality is better 
                if new_quality >= best_quality:
                    best_quality = new_quality 

                # put back the old route if the quality is not better or the same  
                else: 
                    self.network.replace_route(r, old_route)

        return self.network







    