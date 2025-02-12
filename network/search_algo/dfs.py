def dfs_iterative(graph, start_vertex, purpose=None):
    visited = set()
    stack = [[start_vertex]]

    while stack:
        path = stack.pop()
        vertex = path[-1]
        
        if vertex == purpose:
            return path
        
        if vertex not in visited:
            visited.add(vertex)
            
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append(new_path)

    return None

# To check the correctness of the code
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# path = dfs_iterative(graph, 'A', 'F')
# print("Шлях:", path)
