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