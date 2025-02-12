from network.network_tools import *
from network.search_algo.dfs import *
from network.search_algo.bfs import *
from timeit import timeit

graph = {}
# if you want to generate a random graph uncomment the line below
# graph = generate_random_graph(30) # You can change the number of nodes as needed and the file name as well
file_name = "transport_network.graphml" if graph == {} else graph
file = load_graph(file_name)

#G = graph_data(file)

# Перетворюємо граф networkx у список суміжності
graph_dict = {str(node): list(map(str, file.neighbors(node))) for node in file.nodes}


start_G = input("Введіть початкову вершину: ")
end_G = input("Введіть кінцеву вершину: ")

print("DFS:")
path = dfs_iterative(graph_dict, start_G, end_G)
print(path)
print(f"DFS time {timeit(lambda: dfs_iterative(graph_dict, start_G, end_G), number=1):.6f} sec")

print("BFS:")
path = bfs_iterative(graph_dict, start_G, end_G)
print(path)
print(f"BFS time {timeit(lambda: bfs_iterative(graph_dict, start_G, end_G), number=1):.6f} sec")



