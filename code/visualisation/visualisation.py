
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import networkx as nx
import csv



def extract_stations(csv_file):
    """ 
    IN: csv file with stations 
    OUT: list of stations
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
    IN: csv file of connected stations with connection duration
    OUT: list of tuples of form: (station1, station2, distance)
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



########################### visualisation #################################### 

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv

# def visualise(station_list, connections, network_object, label=True):
#     """ 
#     IN: station_list, connections list, network_object, label statement
#     OUT: plot of routes in given network
#     """

#     # Extract x, y coordinates, and station names
#     x = []
#     y = []
#     station_names = []

#     for station in station_list:
#         name, lon, lat = station.split(',')
#         x.append(float(lat))
#         y.append(float(lon))
#         station_names.append(name)

#     # Create the map
#     plt.figure(figsize=(6, 40))

#     # Draw the stations as nodes
#     plt.scatter(x, y, s=30, c='darkblue', marker='o', linewidths=5, zorder=5)

#     all_routes = network_object.routes

    
#     route_lines = []
#     for route in all_routes:
#         new_route = route.route
#         route_lines.append([])
#         for a, b in zip(new_route, new_route[1:]):
#             index_a = station_names.index(a.name)
#             index_b = station_names.index(b.name)
#             route_lines[-1].append((x[index_a], y[index_a], x[index_b], y[index_b]))

#     # keep count of lines, and move each line a little 
#     # so that lines will not overlap exactly
#     mv_line = 0


#     # Draw the connections between stations 
#     for lines, color in zip(route_lines, mcolors.TABLEAU_COLORS):

#         move_count = 0
        
#         for x1, y1, x2, y2 in lines:

#             # apply slight change to coordinate values 
#             move_count += 1 

#             if move_count == 1: 
#                 plt.plot([x1 + 0.01, x2], [y1, y2], color=color, linewidth=2)

#             if move_count == 2: 
#                  plt.plot([x1, x2 + 0.01], [y1, y2], color=color, linewidth=2)

#             if move_count == 3:
#                 plt.plot([x1, x2], [y1 + 0.01, y2], color=color, linewidth=2)
 
#             if move_count == 4: 
#                 plt.plot([x1, x2], [y1, y2 + 0.01], color=color, linewidth=2)

#             # reset counter after all coordinates have been changed
#             if move_count == 4: 
#                 move_count = 0

                
#     # Add labels to the stations ######################################
#     if label: 
#         for i, (x_val, y_val) in enumerate(zip(x, y)):
#             plt.text(x_val, y_val, station_names[i], fontsize=4, bbox=dict(facecolor='pink', alpha=0.8), zorder=10)

#     # Set map boundaries
#     plt.xlim(min(x) - 0.05, max(x) + 0.05)
#     plt.ylim(min(y) - 1, max(y) + 1)

#     # use map of nl as background
#     img = plt.imread("nl_map.png")
#     plt.imshow(img, aspect='auto')

#     # Add gridlines and title
#     plt.grid(True)
#     plt.title("Stations Map")


#     plt.savefig('code/visualisation/plots/map.png')

#     # Show the map
#     plt.show()




################### edit of visualisation ############################## 

# def visualise(station_list, connections, network_object, label=True):
#     """ 
#     IN: station_list, connections list, network_object, label statement
#     OUT: plot of routes in given network
#     """

#     # Extract x, y coordinates, and station names
#     x = []
#     y = []
#     station_names = []

#     for station in station_list:
#         name, lon, lat = station.split(',')
#         x.append(float(lat))
#         y.append(float(lon))
#         station_names.append(name)

#     # Create the map
#     fig = plt.figure()
#     ax = fig.add_subplot(1000)

#     map_nl = plt.imread("blank_map.jpg")

#     fig, ax = plt.subplots()

#     plt.imshow(map_nl, extent=[-2, 2, -3, 3])


#     # Draw the stations as nodes
#     plt.scatter(x, y, s=30, c='darkblue', marker='o', linewidths=5, zorder=5)

#     # # use map of nl as background
#     # map_nl = plt.imread("blank_map.jpg")
#     # plt.imshow(map_nl, extent=[-2, 2, -3, 3])
#     # plt.show()


#     all_routes = network_object.routes

    
#     route_lines = []
#     for route in all_routes:
#         new_route = route.route
#         route_lines.append([])
#         for a, b in zip(new_route, new_route[1:]):
#             index_a = station_names.index(a.name)
#             index_b = station_names.index(b.name)
#             route_lines[-1].append((x[index_a], y[index_a], x[index_b], y[index_b]))

#     # keep count of lines, and move each line a little 
#     # so that lines will not overlap exactly
#     mv_line = 0


#     # Draw the connections between stations 
#     for lines, color in zip(route_lines, mcolors.TABLEAU_COLORS):

#         move_count = 0
        
#         for x1, y1, x2, y2 in lines:

#             # apply slight change to coordinate values 
#             move_count += 1 

#             if move_count == 1: 
#                 plt.plot([x1 + 0.01, x2], [y1, y2], color=color, linewidth=2)

#             if move_count == 2: 
#                  plt.plot([x1, x2 + 0.01], [y1, y2], color=color, linewidth=2)

#             if move_count == 3:
#                 plt.plot([x1, x2], [y1 + 0.01, y2], color=color, linewidth=2)
 
#             if move_count == 4: 
#                 plt.plot([x1, x2], [y1, y2 + 0.01], color=color, linewidth=2)

#             # reset counter after all coordinates have been changed
#             if move_count == 4: 
#                 move_count = 0

                
#     # Add labels to the stations ######################################
#     if label: 
#         for i, (x_val, y_val) in enumerate(zip(x, y)):
#             plt.text(x_val, y_val, station_names[i], fontsize=4, bbox=dict(facecolor='pink', alpha=0.8), zorder=10)



#     # Set map boundaries
#     plt.xlim(min(x) - 0.05, max(x) + 0.05)
#     plt.ylim(min(y) - 1, max(y) + 1)

#     # Add gridlines and title
#     # plt.grid(True)

#     plt.title("Stations Map")

#     # use map of nl as background
   
#     # plt.show()


#     plt.savefig('code/visualisation/plots/map.png')

#     # Show the map
#     plt.show()

##############################################

def visualise(station_list, connections, network_object, label=True):
    """ 
    IN: station_list, connections list, network_object, label statement
    OUT: plot of routes in given network
    """

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
    fig = plt.figure()
    ax = fig.add_subplot(111)

    map_nl = plt.imread("data/blank_map.jpg")

    # Draw the stations as nodes
    ax.scatter(x, y, s=30, c='darkblue', marker='o', linewidths=5, zorder=5)

    # Set the extent of the scatterplot to match the image
    ax.set_xlim(min(x) - 0.05, max(x) + 0.05)
    ax.set_ylim(min(y) - 1, max(y) + 1)

    # Show the map as the background
    ax.imshow(map_nl, extent=[min(x) - 0.05, max(x) + 0.05, min(y) - 1, max(y) + 1], aspect='auto', alpha=0.5)

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
                ax.plot([x1 + 0.01, x2], [y1, y2], color=color, linewidth=2)
            if move_count == 2: 
                ax.plot([x1, x2 + 0.01], [y1, y2], color=color, linewidth=2)
            if move_count == 3:
                ax.plot([x1, x2], [y1 + 0.01, y2], color=color, linewidth=2)
            if move_count == 4: 
                ax.plot([x1, x2], [y1, y2 + 0.01], color=color, linewidth=2)
            # reset counter after all coordinates have been changed
            if move_count == 4: 
                move_count = 0

    # Add labels to the stations
    if label: 
        for i, (x_val, y_val) in enumerate(zip(x, y)):
            ax.text(x_val, y_val, station_names[i], fontsize=4, bbox=dict(facecolor='pink', alpha=0.8), zorder=10)

    # Add gridlines and title
    ax.grid(True)
    ax.set_title("Stations Map")

    # Save the plot
    plt.savefig('code/visualisation/plots/map.png')

    # Show the plot
    plt.show()
