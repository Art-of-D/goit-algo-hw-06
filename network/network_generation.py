import networkx as nx
import random

# Generate a random graph
num_nodes = 30
G = nx.Graph()

for i in range(num_nodes):
    G.add_node(i, label=f"Район {i}")

for _ in range(num_nodes * 2):
    u, v = random.sample(range(num_nodes), 2)
    weight = random.randint(1, 10)
    G.add_edge(u, v, weight=weight)

file_name = "new_transport_network.graphml" # Change this to your desired file name
nx.write_graphml(G, file_name)

print(f"Your graph has been saved to {file_name}")

