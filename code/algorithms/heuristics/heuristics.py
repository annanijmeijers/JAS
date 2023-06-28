def max_connections_heuristic(connection_list, station_list):
    '''
    IN: connection_list: connection dictionary {station: duration}
        station_list: list of station objects
    This heuristic is used for obtaining a new station object based
    on the maximum amount of connections it has.
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
    This heuristic is used to obtain a station with using the least amount of cost.
    It calculates these costs based on if connection have already been ridden on.
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
    IN: connection_options: connection dictionary {station: duration}
        station_list: list of station objects
        route_object: Route-Class object
    This heuristic selects the next station based on the shortest 
    distance from the current station. It prioritizes stations that 
    are closer in terms of travel distance. 
    OUT: next_station: station_object or None 
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