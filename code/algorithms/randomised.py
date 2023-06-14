import random

def random_initialise(route_obj):
    """
    IN: Route-object
    Initialises the route by choosing a random Station-object from 
    a list of stations stored in Route
    """
    # choosing the station and adding it to the route
    station = random.choice(route_obj.list_of_stations)
    route_obj.add_station(station)

    return 

def random_connection(route_obj): 
    """
    IN: Route-object 
    Checks possible connections for the last station in the route 
    and picks a random new connection and adds it to the route 
    """
    connection_options = route_obj.check_connection()
    next_connection = random.choice(list(connection_options.keys()))

    route_obj.add_connection(next_connection, connection_options)

    return 

def build_route(route_obj): 
    """
    IN: Route-object 
    Implements random_initialise to initialise the route and implements 
    random_connection until the duration surpasses the timeframe given to the route
    """
    random_initialise(route_obj)
    while route_obj.duration < route_obj.timeframe:
        random_connection(route_obj)

    return  
