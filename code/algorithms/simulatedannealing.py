import copy 
import random 
from ..classes.route import Route 
from ..algorithms.randomised import RandomRoute
from tqdm import tqdm

class SimulatedAnnealing(): 
    """
    Implementation of simulated annealing 
    """

    def __init__(self, network_object, all_stations, starting_temp):
        self.network = copy.deepcopy(network_object) 
        self.all_stations = all_stations 
        self.old_score = self.network.quality()
        self.new_score = None
        self.starting_temp = starting_temp 
        self.temp = starting_temp
        self.route_to_replace = None 
        self.qualities_for_vis = []


    def calculate_accept(self, delta): 

        # add a fail-safe to prevent overflow
        if delta > 1000:  
            return False 

        # add a 1 to the denominator to prevent overlow 
        accept_prob = 2 ** (delta / self.temp + 1)

        # decide to accept or not 
        if random.random() > accept_prob: 
            return True 
        else: 
            return False 
        
    def lower_temp(self, iterations): 

        # use a linear cooling scheme 
        self.temp -=  self.starting_temp / iterations

    def replace_and_test(self, r): 
        # get the old route from the Network 
        self.route_to_replace = self.network.get_route(r)

        # create a new random Route 
        new_route = Route(180, self.all_stations) 
        RandomRoute(new_route).build_route()

        # replace the route and calculate the new quality 
        self.network.replace_route(r, new_route)
        self.new_score = self.network.quality()

        delta = self.old_score - self.new_score 

        return delta 
    
    def run(self, iterations): 
 
        for i in tqdm(range(iterations)): 

            # choose a random route to change 
            route_to_replace = random.choice(self.network.routes)
            number_of_route = route_to_replace.number

            delta = self.replace_and_test(number_of_route) 
            accept = self.calculate_accept(delta)

            # either accept or put the old route back 
            if accept:
                self.old_score = self.new_score
            else: 
                self.network.replace_route(number_of_route, self.route_to_replace) 
            
            self.qualities_for_vis.append(self.old_score)

            self.lower_temp(iterations)
            
            
            
            
            







    
    



