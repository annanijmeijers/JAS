import networkx as nx
import matplotlib.pyplot as plt 

# create empty graph 
G = nx.Graph()

# add all station and coordinates in list 
station_list = [
    "Alkmaar,52.63777924,4.739722252",
    "Alphen a/d Rijn,52.12444305,4.657777786",
    "Amsterdam Amstel,52.34666824,4.917778015",
    "Amsterdam Centraal,52.37888718,4.900277615",
    "Amsterdam Sloterdijk,52.38888931,4.837777615",
    "Amsterdam Zuid,52.338889,4.872356",
    "Beverwijk,52.47833252,4.656666756",
    "Castricum,52.54583359,4.658611298",
    "Delft,52.00666809,4.356389046",
    "Den Haag Centraal,52.08027649,4.324999809",
    "Den Helder,52.95527649,4.761111259",
    "Dordrecht,51.80722046,4.66833353",
    "Gouda,52.01750183,4.704444408",
    "Haarlem,52.38777924,4.638333321",
    "Heemstede-Aerdenhout,52.35916519,4.606666565",
    "Hoorn,52.64472198,5.055555344",
    "Leiden Centraal,52.16611099,4.481666565",
    "Rotterdam Alexander,51.95194626,4.553611279",
    "Rotterdam Centraal,51.92499924,4.46888876",
    "Schiedam Centrum,51.92124381,4.408993721",
    "Schiphol Airport,52.30944443,4.761944294",
    "Zaandam,52.43888855,4.813611031"
]

# add stations in list as nodes 
for station in station_list:
    name, x, y = station.split(",")
    G.add_node(name, pos=(float(x), float(y)))

plt.show()