
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv
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
        # save stations in list 
        self.stations = []

        # read csv_file with stations
        with open(self.station_list_csv, 'r') as file:

            reader = csv.reader(file)
            next(reader)

            for row in reader:

                # assuming the csv file has three columns: name, latitude, and longitude
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

        # save connections in list
        self.connections = []

        # read csv_file with connections
        with open(self.connection_list_csv, 'r') as file:

            reader = csv.reader(file)
            next(reader)

            # assuming the csv file has three columns: station1, station2, distance
            for row in reader:
                station1 = row[0]
                station2 = row[1]
                distance = float(row[2])
                self.connections.append((station1, station2, distance))

        
    def extract_data(self, station_list_csv, connection_list_csv): 
        """ 
        IN: csv file with stations, csv file with connections
        OUT: station_list and connections_list
        """

        self.station_list_csv = station_list_csv
        self.connection_list_csv = connection_list_csv
        self.extract_stations()
        self.read_connections()
        

    def visualise(self, network_object, label=False, title=True):
        """ 
        IN: network_object (optional bools: label, title)
        OUT: plot of routes in given network
        """

        # print warning and return function if there is no data loaded yet 
        if not self.stations and not self.connections: 
            print('WARNING: NO DATA YET -- first load the data with extract_data()')
            return 

        # extract x, y coordinates, and station names
        x = []
        y = []
        self.station_names = []

        # append coordinates and stations to lists 
        for station in self.stations:
            name, lon, lat = station.split(',')
            x.append(float(lat))
            y.append(float(lon))
            self.station_names.append(name)

        # create the map
        plt.figure()
    
        # draw the stations as nodes
        plt.scatter(x, y, s=3, c='darkblue', marker='o', linewidths=5, zorder=5)
        plt.xlim(min(x) - 0.2, max(x) + 0.2)
        plt.ylim(min(y) - 0.3, max(y) + 0.3)

    
        # obtain all routes
        all_routes = network_object.routes

        # save lines between routes in list
        route_lines = []

        # loop over routes and save empty list for route lines
        for route in all_routes:
            new_route = route.route
            route_lines.append([])

            # determine route line and append coordinates to route_lines
            for a, b in zip(new_route, new_route[1:]):
                index_a = self.station_names.index(a.name)
                index_b = self.station_names.index(b.name)
                route_lines[-1].append((x[index_a], y[index_a], x[index_b], y[index_b]))


        # draw the connections between stations which different colors for each 
        for lines, color in zip(route_lines, mcolors.XKCD_COLORS):

            # keep count of lines, and move each line a little 
            # so that lines will not overlap exactly
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

        # add labels to the stations if asked for 
        if label: 
            for i, (x_val, y_val) in enumerate(zip(x, y)):
                plt.text(x_val, y_val, self.station_names[i], fontsize=4, bbox=dict(facecolor='pink', alpha=0.8), zorder=10)

        # add title if asked for 
        if title: 
            plt.title(f'Railnet with {network_object}')

        # add gridlines and title
        plt.grid(True)
        
        # save the plot
        plt.savefig(f'code/visualisation/plots/{network_object}.png')

        # show the plot
        plt.show()
