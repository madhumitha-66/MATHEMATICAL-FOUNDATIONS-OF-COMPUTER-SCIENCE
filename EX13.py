from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'C', 'F'],
    'F': ['D', 'E']
}

def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node == goal:
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    if goal not in parent:
        print("No route found")
        return

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Traversal Order:", order)
    print("Shortest Path:", path)
    print("Corridors:", len(path) - 1)


bfs('A', 'F')
