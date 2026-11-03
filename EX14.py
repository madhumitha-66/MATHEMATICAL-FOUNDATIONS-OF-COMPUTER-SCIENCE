vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D'),
    (6, 'C', 'E'),
    (7, 'D', 'E')
]

parent = {v: v for v in vertices}

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a
        return True

    return False


edges.sort()

mst = []
total = 0

for weight, u, v in edges:
    if union(u, v):
        mst.append((u, v, weight))
        total += weight

print("Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "-", v, ":", weight)

print("\nTotal Installation Cost:", total)
