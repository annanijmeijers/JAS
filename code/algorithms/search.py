import copy

class BreadthFirst:
    """
    A Breadth First algorithm that builds a route with unique
    connections for each route.
    """
    def __init__(self, station_list, route_obj):
        self.station_list = station_list # hiernaar kijken ivm begin station aanpassen wellicht geen deepcopy nodig
        self.list_of_states = [copy.deepcopy(route_obj)]
        self.route_obj = None
        self.states = 0

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.list_of_states.pop(0)

    def build_child_states(self, route_obj, connections):
        """
        Creates all possible child-states and adds them to the list of states.
        """

        # add a route instance to the list of states if the route is valid
        for connection, time in connections.items():
            new_route = copy.deepcopy(route_obj)
            new_route.add_connection(connection, connections)
            if new_route.duration <= new_route.timeframe:
                self.states += 1
                self.list_of_states.append(new_route)
            else:
                break
    

    def run(self):
        """
        runs the algorithm until all possible states are visited.
        """
        while self.list_of_states:
            new_route = self.get_next_state()

            # Retrieve all valid possible connections for the node.
            connections = new_route.check_connection()

            if connections:
                self.build_child_states(new_route, connections)
            else:
                # stop if we find a solution (breadth first search)
                break
                
                # continue looking for a better solution (best first search)
        self.route_obj = new_route

class DepthFirst(BreadthFirst):

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.list_of_states.pop()        
        

    
