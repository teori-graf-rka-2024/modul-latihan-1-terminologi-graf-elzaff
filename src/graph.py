import networkx as nx
import matplotlib.pyplot as plt

# 1.. create_graph
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

#2. get_degree
def get_degree(G: nx.Graph, node: int) -> int:
    if node not in G:
        raise ValueError(f"Node {node} tidak ditemukan dalam graf.")
    return G.degree[node]

#3. dfs_traversal
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    if start not in G:
        raise ValueError(f"Node {start} tidak ditemukan dalam graf.")
    return list(nx.dfs_preorder_nodes(G, start))

#4. bfs_traversal
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_tree(G, start).nodes)

#5. find_shortest_path
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source=source, target=target)

#6. visualize_graph
def visualize_graph(G: nx.Graph) -> None:
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
    plt.savefig("graph_visualization.png")
    plt.show()
