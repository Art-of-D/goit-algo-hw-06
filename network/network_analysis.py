import matplotlib.pyplot as plt
import networkx as nx

file_name = "transport_network.graphml" # Change this to your desired file name
G_loaded = nx.read_graphml(f"./network/{file_name}")
G = nx.Graph(G_loaded)

# Graph visualization
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Центральність ступеня:{degree_centrality}")
print(f"Близькість вузлів:{closeness_centrality}")
print(f"Посередництво вузлів:{betweenness_centrality}")
print("Ступінь кожної вершини:")
for node, degree in degrees.items():
    print(f"- Вершина {node}: ребер {degree}")
    

plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color='green', edge_color='black', node_size=2000, font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title(file_name)
plt.show()