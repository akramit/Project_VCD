import random
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

def generate_random_graph(n):
    """
    Generate a random graph with n vertices and output its adjacency list.
    Args:
        n (int): Number of vertices (1 to n).
    """
    adjacency_list = [set([i]) for i in range(1, n + 1)]
    no_of_edges = (n * (n-1)) / 2 
    random_no_of_edges = random.randint(0, no_of_edges)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"graph_{timestamp}.txt"
    with open(filename, "w") as file:
        file.write(f"#  {n} node graph\n")
        for i in range(1, n):
            for j in range(i+1, n + 1) : 
                edge_exists = random.choice([True, False])
                if (edge_exists) : 
                    file.write(f"{i} {j}\n")
                    adjacency_list[i-1].add(j)
                    adjacency_list[j-1].add(i)

    return adjacency_list, filename


def visualize_graph(adjacency_list):
    G = nx.Graph()
    for i, neighbors in enumerate(adjacency_list):
        for neighbor in neighbors:
            G.add_edge(i + 1, neighbor)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    plt.show()

#Example usage
if __name__ == "__main__":
    n = 6  # Number of vertices
    random_graph = generate_random_graph(n)
    print("Random Graph Adjacency List:", random_graph)

# if __name__ == "__main__":
#     n = 26  # Number of vertices
#     random_graph = generate_random_graph(n)
#     print("Random Graph Adjacency List:", random_graph)
#     visualize_graph(random_graph)

def generate_set_system_from_graph_adjacency_list(graph): 
    return null

def generate_set_system_from_graph_adjacency_matrix(graph):
    return null