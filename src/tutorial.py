import networkx as nx
from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

# .Data edges untuk graf
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8)]

# Membuat graf
G = create_graph(edges)

# Menghitung derajat simpul tertentu
node = 2
print(f"Degree of node {node}: {get_degree(G, node)}")

# DFS
start_node = 1
print(f"DFS dari node {start_node}: {dfs_traversal(G, start_node)}")

# BFS
print(f"BFS dari node {start_node}: {bfs_traversal(G, start_node)}")

# Menentukan jalur terpendek antara dua simpul
source, target = 1, 8
print(f"Jarak terpendek dari {source} ke {target}: {find_shortest_path(G, source, target)}")

# Visualisasi graf
visualize_graph(G)
