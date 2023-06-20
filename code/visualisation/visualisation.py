
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



# def visualise(station_list, connections, network_object):
        
#     # Create a graph object
#     G = nx.Graph()

#     # Extract x, y coordinates, and station names
#     x = []
#     y = []
#     station_names = []

#     for station in station_list:
#         name, lon, lat = station.split(',')
#         if name in G.nodes: 
#             continue
#         x.append(float(lat))
#         y.append(float(lon))
#         station_names.append(name)

#         # Add nodes to the graph
#         G.add_node(name, pos=(float(lat), float(lon)))



#     # Create the map
#     plt.figure(figsize=(8, 20))

#     # Draw the stations as nodes
#     pos = {name: (lon, lat) for name, lon, lat in zip(station_names, x, y)}
#     nx.draw_networkx_nodes(G, pos, node_size=80, node_color='skyblue', node_shape='s', linewidths=20)

#     all_routes = network_object.routes 
#     colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
#     for route in all_routes:  
#             new_route = route.route 

#             for a, b in zip(new_route, new_route[1:]):
#                 G.add_edge(a.name, b.name)


#     # Add labels to the stations
#     labels = {name: name for name in station_names}
#     nx.draw_networkx_labels(G, pos, labels, font_size=8)

#     # Draw the connections between stations as edges
#     nx.draw_networkx_edges(G, pos, width=2, edge_color=colors)

#     # Set map boundaries
#     plt.xlim(min(x) - 0.05, max(x) + 0.05)
#     plt.ylim(min(y) - 0.03, max(y) + 0.03)

#     # Add gridlines and title
#     plt.grid(True)
#     plt.title("Stations Map")
#     plt.savefig('code/visualisation/plots/map.png')

#     # Show the map
#     plt.show()




########################### test code change #################################### 

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv

def visualise(station_list, connections, network_object):
    # Extract x, y coordinates, and station names
    x = []
    y = []
    station_names = []

    for station in station_list:
        name, lon, lat = station.split(',')
        x.append(float(lat))
        y.append(float(lon))
        station_names.append(name)

    # Create the map
    plt.figure(figsize=(8, 20))

    # Draw the stations as nodes
    plt.scatter(x, y, s=60, c='pink', marker='o', linewidths=5)

    all_routes = network_object.routes

    
    route_lines = []
    for route in all_routes:
        new_route = route.route
        route_lines.append([])
        for a, b in zip(new_route, new_route[1:]):
            index_a = station_names.index(a.name)
            index_b = station_names.index(b.name)
            route_lines[-1].append((x[index_a], y[index_a], x[index_b], y[index_b]))

    # keep count of lines, and move each line a little 
    # so that lines will not overlap exactly
    mv_line = 0


    # Draw the connections between stations 
    for lines, color in zip(route_lines, mcolors.TABLEAU_COLORS):

        move_count = 0
        
        for x1, y1, x2, y2 in lines:

            # apply slight change to coordinate values 
            move_count += 1 

            if move_count == 1: 
                plt.plot([x1 + 0.01, x2], [y1, y2], color=color, linewidth=2)

            if move_count == 2: 
                 plt.plot([x1, x2 + 0.01], [y1, y2], color=color, linewidth=2)

            if move_count == 3:
                plt.plot([x1, x2], [y1 + 0.01, y2], color=color, linewidth=2)
 
            if move_count == 4: 
                plt.plot([x1, x2], [y1, y2 + 0.01], color=color, linewidth=2)

            # reset counter after all coordinates have been changed
            if move_count == 4: 
                move_count = 0

                
    # Add labels to the stations
    for i, (x_val, y_val) in enumerate(zip(x, y)):
        plt.text(x_val, y_val, station_names[i], fontsize=8)

    # Set map boundaries
    plt.xlim(min(x) - 0.05, max(x) + 0.05)
    plt.ylim(min(y) - 1, max(y) + 1)

    # use map of nl as background
    # img = plt.imread("nl_map.png")
    # plt.imshow(img, extent=[0, 15, 30, 70])

    # Add gridlines and title
    plt.grid(True)
    plt.title("Stations Map")


    plt.savefig('code/visualisation/plots/map.png')

    # Show the map
    plt.show()

