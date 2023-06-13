
import matplotlib.pyplot as plt
import networkx as nx
import csv


def extract_stations(csv_file):
    stations = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the CSV file has three columns: name, latitude, and longitude
            name = row[0]
            longitude = row[1]
            latitude = row[2]
            station = f"{name},{longitude},{latitude}"
            stations.append(station)
    return stations

# Create list with stations
csv_file = 'StationsNationaal.csv' 
station_list = extract_stations(csv_file)
print(station_list)

def read_connections(csv_file):
    connections = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            station1 = row[0]
            station2 = row[1]
            distance = float(row[2])
            connections.append((station1, station2, distance))
    return connections

# Create list with connections
csv_file_connections = 'ConnectiesNationaal.csv'
connections = read_connections(csv_file_connections)
print(connections)

  
import networkx as nx
import matplotlib.pyplot as plt

def visualise(station_list, connections):
    """ 
    This function accepts a list of stations and a 
    list of connections made. It then proceeds to 
    map the connections made between the stations. 
    """
    # Create a graph object
    G = nx.Graph()

    # Extract x, y coordinates, and station names
    x = []
    y = []
    station_names = []
    for station in station_list:
        name, lon, lat = station.split(',')
        x.append(float(lon))
        y.append(float(lat))
        station_names.append(name)

        # Add nodes to the graph
        G.add_node(name, pos=(float(lon), float(lat)))

    # Change the way connection list is given
    new_connections = []
    for connection in connections:
        connection = connection.strip('[]').split(', ')

        for i in range(len(connection) - 1):
            station1 = next(station for station in station_list if station.startswith(connection[i]))
            station2 = next(station for station in station_list if station.startswith(connection[i + 1]))
            distance = 1  # Placeholder distance, you can change it based on your data
            new_connections.append((station1, station2, distance))

    # Add edges to the graph with distances as weights
    for connection in new_connections:
        station1, station2, distance = connection
        G.add_edge(station1, station2)

    # Create the map
    plt.figure(figsize=(10, 8))

    # Draw the stations as nodes
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='yellow', node_size=100, edgecolors='black')

    # Draw the connections between stations as edges
    nx.draw_networkx_edges(G, pos, width=1)

    # Add labels to the stations
    labels = {name: name for name in station_names}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    # Set map boundaries
    plt.xlim(min(x) - 0.03, max(x) + 0.03)
    plt.ylim(min(y) - 0.03, max(y) + 0.03)

    # Add gridlines and title
    plt.grid(True)
    plt.title("Stations Map")

    return plt.show()







route_1 = "[Schiedam Centrum, Delft, Den Haag Centraal, Gouda, Rotterdam Alexander, Rotterdam Centraal, Dordrecht]"
route_2 = "[Beverwijk, Haarlem, Heemstede-Aerdenhout, Leiden Centraal, Schiphol Airport, Amsterdam Zuid, Amsterdam Sloterdijk]"
route_3 = "[Amsterdam Zuid, Schiphol Airport, Leiden Centraal, Alphen a/d Rijn, Gouda, Den Haag Centraal]"

connections = [route_1, route_2, route_3]

print(visualise(station_list, connections))




