# Array of Edges (Directed) [Start, End]
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Convert Array of Edges -> Adjacency Matrix

M = []
for i in range(n):
    M.append([0] * n)

for u, v in A:
    M[u][v] = 1
    # Uncomment the following line if the graph is undirected
    # M[v][u] = 1

# Convert Array of Edges -> Adjacency List
# Convert Array of Edges -> Adjacency List
from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    # Uncomment the following line if the graph is undirected
    # D[v].append(u)

print(D)

# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges

def dfs_recursive(node):
    # print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

source = 0
seen = set()
seen.add(source)
dfs_recursive(source)

# Iterative DFS - O(V+E) 
source = 0
stack = [source]
seen = set()
seen.add(source)

while stack:
    node = stack.pop()
    # print(node)
    for e in D[node]:
        if e not in seen:
            seen.add(e)
            stack.append(e)

# BFS
from collections import deque

source = 0
q = deque([0])
seen = set()
seen.add(source)
while q:
    node = q.popleft()
    print(node)
    for n in D[node]:
        if n not in seen:
            seen.add(n)
            q.append(n)

