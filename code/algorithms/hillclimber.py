from randomised import RandomRoute
from ..classes import route 
import tqdm 

class NetClimber(): 

    def __init__(self, network_object, all_stations):
        self.all_stations = all_stations 
        self.network_object = network_object
        self.original_quality = network_object.quality()

    def run(self, tries_per_route=100):
        for r in tqdm(range(1, len(self.network_object.routes)+1), desc='Routes'): 
            best_quality = self.original_quality
        

            for t in tqdm(range(tries_per_route), desc='Tries'): 

                # get the old route from the Network 
                old_route = self.network_object.get_route(r)

                # create a new random Route 
                new_route = route.Route(180, self.all_stations) 
                RandomRoute(new_route).build_route()

                # replace the route and calculate the new quality 
                self.network_object.replace_route(r, new_route)
                new_quality = self.network_object.quality()

                # check if the quality is better 
                if new_quality > best_quality:
                    best_quality = new_quality 

                # put back the old route if the quality is not better 
                else: 
                    self.network_object.replace_route(r, old_route)
                    







    