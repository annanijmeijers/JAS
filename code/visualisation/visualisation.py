
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import numpy as np 
import networkx as nx
import csv
 

# from classes import network
from code.classes.network import Network
from code.classes.route import Route




class Visualisation(): 
    def __init__(self): 
        self.stations = None
        self.connections = None
        self.station_list_csv = None
        self.connection_list_csv = None 
        self.label = True 
        
        
    def extract_stations(self): 

        """ 
        IN: csv file with stations 
        OUT: list of stations
        """
        # Save stations in list 
        self.stations = []

        # Read csv_file with stations
        with open(self.station_list_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:

                # Assuming the CSV file has three columns: name, latitude, and longitude
                name = row[0]
                longitude = row[1]
                latitude = row[2]
                station = f"{name},{longitude},{latitude}"

                self.stations.append(station)

        

    def read_connections(self): 
        """ 
        IN: csv file of connected stations with connection duration
        OUT: list of tuples of form: (station1, station2, distance)
        """

        # Save connections in list
        self.connections = []

        # read csv_file with connections
        with open(self.connection_list_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                station1 = row[0]
                station2 = row[1]
                distance = float(row[2])
                self.connections.append((station1, station2, distance))

        

    def extract_data(self, station_list_csv, connection_list_csv): 
        """ 
        calls extract_stations and read_connections and 
        returns station_list and connections_list

        """
        self.station_list_csv = station_list_csv
        self.connection_list_csv = connection_list_csv
        self.extract_stations()
        self.read_connections()
        

    def visualise(self, network_object, label=True, title=True):
        """ 
        IN: station_list, connections list, network_object, label statement
        OUT: plot of routes in given network
        """

        if not self.stations and not self.connections: 
            print('WARNING: NO DATA YET -- first load the data with extract_data()')
            return 

        # Extract x, y coordinates, and station names
        x = []
        y = []
        self.station_names = []


        for station in self.stations:
            name, lon, lat = station.split(',')
            x.append(float(lat))
            y.append(float(lon))
            self.station_names.append(name)

        # Create the map
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Set map of NL as background
        map_nl = plt.imread('data/blank_map.jpg')
        

        # Draw the stations as nodes
        ax.scatter(x, y, s=30, c='darkblue', marker='o', linewidths=5, zorder=5)

        # Set the extent of the scatterplot to match the image
        ax.set_xlim(min(x) - 0.05, max(x) + 0.05)
        ax.set_ylim(min(y) - 1, max(y) + 1)

        # Show the map as the background
        ax.imshow(map_nl, extent=[min(x) - 0.05, max(x) + 0.05, min(y) - 1, max(y) + 1], aspect='auto', alpha=0.5)

        # Obtain all routes s
        all_routes = network_object.routes

        # Save lines between routes in list
        route_lines = []

        for route in all_routes:
            new_route = route.route
            route_lines.append([])
            for a, b in zip(new_route, new_route[1:]):
                index_a = self.station_names.index(a.name)
                index_b = self.station_names.index(b.name)
                route_lines[-1].append((x[index_a], y[index_a], x[index_b], y[index_b]))


        # Draw the connections between stations 
        for lines, color in zip(route_lines, mcolors.TABLEAU_COLORS):

            # keep count of lines, and move each line a little 
            # so that lines will not overlap exactly
            move_count = 0

            for x1, y1, x2, y2 in lines:

                # Apply slight change to coordinate values 
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

        # Add labels to the stations if asked for 
        if label: 
            for i, (x_val, y_val) in enumerate(zip(x, y)):
                ax.text(x_val, y_val, self.station_names[i], fontsize=4, bbox=dict(facecolor='pink', alpha=0.8), zorder=10)

        # Add title if asked for 
        if title: 
            ax.set_title(f'Railnet with {network_object}')

        # Add gridlines and title
        ax.grid(True)
        
        # Save the plot
        # plt.savefig(f'code/visualisation/plots/{network_object}.png')

        # Show the plot
        plt.show()


########################### visualisation #################################### 

# 'data/StationsHolland.csv'
# 'data/ConnectiesHolland.csv'

# vis = Visualisation()

# # test visualisation
# vis.extract_data(station_list_csv='StationsHolland.csv', connection_list_csv='ConnectiesHolland.csv')


# # initialise a network, give it the total ammount of connections  
# rail_net = network.Network(28, 7)

# # visualisation 

# vis.visualise(rail_net)
