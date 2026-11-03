import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('D', 2)]
}

def dijkstra(start, goal):
    pq = [(0, start)]
    distance = {start: 0}
    parent = {start: None}

    while pq:
        dist, node = heapq.heappop(pq)

        if node == goal:
            break

        if dist > distance[node]:
            continue

        for neighbour, weight in graph[node]:
            new_dist = dist + weight

            if new_dist < distance.get(neighbour, float('inf')):
                distance[neighbour] = new_dist
                parent[neighbour] = node
                heapq.heappush(pq, (new_dist, neighbour))

    if goal not in distance:
        print("No path found")
        return

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Shortest Path:", path)
    print("Total Distance:", distance[goal])


dijkstra('A', 'E')
