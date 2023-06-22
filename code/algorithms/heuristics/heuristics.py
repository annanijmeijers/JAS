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

    if not choices:
        return False

    return choices

def connection_heuristic(route_obj, station_list):

    count_connections =[]
    stations = []

    # this gives a dictionary with connection options 
    connection_options = route_obj.check_connection()

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
