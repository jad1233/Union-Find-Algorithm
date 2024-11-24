def initialize(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
