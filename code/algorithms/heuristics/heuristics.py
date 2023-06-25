import math

def choice_heuristic(dictionary, heuristic, route_obj, network_obj):
    """
    IN: - dictionary: Dictionary object that contains the destinations
        - heuristic: heuristic used for chosing destinations
        - route_obj: Route object
        - network_obj: Network object
    heuristic choices: 
        - station_based: choices based on stations in route
        - unique_based: choices based on unique connections in network
    This method uses a choice heuristic on the input dictionary to 
    create a list of destination options.
    OUT: - choices: List object that contains (updated)destination options
    """
    choices = list()
    if heuristic == 'station_based':
        for station in dictionary.keys():
            if station not in route_obj.route:
                choices.append(station)
    
    if heuristic == 'unique_based':
        network_obj.calculate_unique_connections()
        for station_name in dictionary.keys():
            if ((station_name, route_obj.route[-1].name) not in network_obj.unique_tracks) or ((route_obj.route[-1].name, station_name) not in network_obj.unique_tracks):
                choices.append(station_name)

    if heuristic == 'distance_based': 
        # current_station = route_obj.route[-1]
        # connection_options = current_station.connections
        
        # choices = distance_based_heuristic(dictionary, connection_options, route_obj)

        for station in dictionary.keys():
            if station not in route_obj.route:
                choices.append(station)

    if not choices:
        return False

    return choices

def max_connections_heuristic(connection_list, station_list):
    '''
    IN: connection_list: connection dictionary {station: duration}
        station_list: list of station objects
    ##uitleg heuristiek
    OUT: max_connections_station: station_object or None
    '''

    count_connections =[]
    stations = []

    # this gives a dictionary with connection options 
    connection_options = connection_list

    # for every key in dict
    for key in connection_options.keys(): 

        # loop through each station in the station objects list
        for station in station_list: 

            # checks if a station in connections is equal to a station in station objects list
            if key == station.name: 

                # appends stations object and station connnection count to seperate lists
                count_connections.append(station.connections_count)
                stations.append(station)

    if count_connections:
            max_index = count_connections.index(max(count_connections))
            max_connections_station = stations[max_index]
            return max_connections_station
    else:
        return 

def unique_connections_heuristic(connection_options, station_list, route_object, network_object):
    '''
    IN: connection_options: connection dictionary {station: duration}
        station_list: list of station objects
        route_object: Route-Class object
        network_object: Network-Class object
    ##uitleg heuristiek
    OUT: next_station: station_object or None 
    '''

    connection_dict = dict()
    current_station = route_object.route[-1]
    next_station = False
    cost = 0
    if not connection_options:
        route_object.end_route = True
        return
    
    # compute next station for the first route
    if not network_object.routes:
        if len(route_object.route) < 2:
            # picks first station with even connections
            if not next_station:
                for connection in connection_options.keys():
                    for station in station_list:
                        if connection == station.name and station.connections_count % 2 == 0:
                            next_station = station
                            cost = 1
            if not next_station:
                for connection in connection_options.keys():
                    for station in station_list:
                        if connection == station.name:
                            next_station = station
                            cost = 1
        else:
            route_object.compute_covered_connections()
            for connection in connection_options.keys():
                if (current_station.name, connection) not in route_object.connection_set and (connection, current_station.name) not in route_object.connection_set:
                    connection_dict[connection] = 1
                else:
                    connection_dict[connection] = 10

            # sort the dict from lowest value to highest value, grab first lowest value
            next_station, cost = sorted(connection_dict.items(), key=lambda x:x[1])[0]

            for station in station_list:
                if next_station == station.name:
                    next_station = station
    
    # compute next station when there are other existing routes
    else:   
        for connection in connection_options.keys():
            if len(route_object.route) < 2:               
                if (current_station.name, connection) not in network_object.covered_tracks:
                    connection_dict[connection] = 1
                else:
                    connection_dict[connection] = 10
            else:
                route_object.compute_covered_connections()
                if (current_station.name, connection) not in network_object.covered_tracks and (current_station.name, connection) not in route_object.connection_set and (connection, current_station.name) not in route_object.connection_set:
                    connection_dict[connection] = 1
                else:
                    connection_dict[connection] = 10                    
            
            next_station, cost = sorted(connection_dict.items(), key=lambda x:x[1])[0]

            for station in station_list:
                if next_station == station.name:
                    next_station = station
    
    if next_station == False:
        return
    return next_station



def distance_based_heuristic(connection_options, station_list, route_object): 

    """
    This heuristic selects the next station based on the shortest 
    distance from the current station. It prioritizes stations that 
    are closer in terms of travel distance. 

    """

    current_station = route_object.route[-1]
    min_distance = float('inf')
    next_station = False 

    for connection in connection_options.keys():
        for station in station_list: 
            if connection == station.name and station != current_station: 
                distance = connection_options[connection]
                
                if distance < min_distance: 
                    min_distance = distance 
                    next_station = station 

    if next_station is False: 
        return  
    return next_station



