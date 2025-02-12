def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    
    previous_nodes = {vertex: None for vertex in graph.nodes}

    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if current_vertex == end:
            break

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]["weight"]
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_vertex

        visited.append(current_vertex)
        unvisited.remove(current_vertex)


    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path if path[0] == start else None