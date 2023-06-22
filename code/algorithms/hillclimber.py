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
        self.qualities_for_vis = None
        self.improvements = None 
    
    def run(self, tries_per_route=100):

        self.qualities_for_vis = []

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
                self.qualities_for_vis.append(best_quality)

                # check if the quality is better 
                if new_quality >= best_quality:
                    best_quality = new_quality 

                # put back the old route if the quality is not better or the same  
                else: 
                    self.network.replace_route(r, old_route)

        return self.network

class StochasticClimber(RailClimber): 

    def run(self, max_cycles): 

        old_score = self.network.quality()
        stop_trying = False
        cycle_count = 0 
        self.improvements = []
        self.qualities_for_vis = []
        pbar = tqdm()

        while not stop_trying: 

            # choose a random route to change 
            route_to_change = random.choice(self.network.routes)
            number_of_route = route_to_change.number 

            # create a new route to swap 
            new_route = Route(180, self.all_stations) 
            RandomRoute(new_route).build_route()

            # replace the route and calculate the new quality 
            self.network.replace_route(number_of_route, new_route)
            new_score = self.network.quality()
            

            improvement = new_score - old_score
            self.improvements.append(improvement)

            if improvement < 0:

                # put the original route back
                self.network.replace_route(number_of_route, route_to_change)

            else: 
                old_score = new_score

            self.qualities_for_vis.append(old_score)   
                
            cycle_count += 1 
            if cycle_count == max_cycles: 
                stop_trying = True 
            
            pbar.update(1)

        pbar.close
            
            
                
            











    