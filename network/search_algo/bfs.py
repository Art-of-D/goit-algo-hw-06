from collections import deque

def bfs_iterative(graph, start, purpose):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]
        
        if purpose == vertex:
            return path
        
        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)

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
# path = bfs_iterative(graph, 'A', 'F')
# print("Шлях:", path)