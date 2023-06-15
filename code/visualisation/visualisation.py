
import matplotlib.pyplot as plt
import networkx as nx
import csv



def extract_stations(csv_file):
    """ 
    pre: csv file with stations 
    post: list of stations
    """
    stations = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:

            # Assuming the CSV file has three columns: name, latitude, and longitude
            name = row[0]
            longitude = row[1]
            latitude = row[2]
            station = f"{name},{longitude},{latitude}"
            stations.append(station)
    return stations


def read_connections(csv_file):
    """ 
    pre: csv file of connected stations with connection duration
    post: list of tuples of form: (station1, station2, distance)
    """
    connections = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            station1 = row[0]
            station2 = row[1]
            distance = float(row[2])
            connections.append((station1, station2, distance))
    return connections



def visualise(station_list, connections, network_object):
        
    # Create a graph object
    G = nx.Graph()

    # Extract x, y coordinates, and station names
    x = []
    y = []
    station_names = []

    for station in station_list:
        name, lon, lat = station.split(',')
        if name in G.nodes: 
            continue
        x.append(float(lat))
        y.append(float(lon))
        station_names.append(name)

        # Add nodes to the graph
        G.add_node(name, pos=(float(lat), float(lon)))

    print(G.nodes)

    # Create the map
    plt.figure(figsize=(8, 20))

    # Draw the stations as nodes
    pos = {name: (lon, lat) for name, lon, lat in zip(station_names, x, y)}
    nx.draw_networkx_nodes(G, pos, node_color='yellow', node_size=100, edgecolors='black')

    all_routes = network_object.routes 
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', '0.5', '0.75', '0.25', '0.1', '0.9', '0.3', '0.7', '0.2', '0.8', '0.4', '0.6', '0.0']

    for route in all_routes:  
            new_route = route.route 

            for a, b in zip(new_route, new_route[1:]):
                G.add_edge(a.name, b.name)


    # Add labels to the stations
    labels = {name: name for name in station_names}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    # Draw the connections between stations as edges
    nx.draw_networkx_edges(G, pos, width=2, edge_color=colors)

    # Set map boundaries
    plt.xlim(min(x) - 0.05, max(x) + 0.05)
    plt.ylim(min(y) - 0.03, max(y) + 0.03)

    # Add gridlines and title
    plt.grid(True)
    plt.title("Stations Map")

    # Show the map
    plt.show()


