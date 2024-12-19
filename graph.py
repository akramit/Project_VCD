import random

def generate_random_graph(n):
    """
    Generate a random graph with n vertices and output its adjacency list.
    Args:
        n (int): Number of vertices (1 to n).
    """
    adjacency_list = [set([i]) for i in range(1, n + 1)]
    no_of_edges = (n * (n-1)) / 2 
    random_no_of_edges = random.randint(0, no_of_edges)


    for i in range(1, random_no_of_edges + 1):
        edge = random.sample(range(1, n+1), 2)
        adjacency_list[edge[0]-1].add(edge[1])
        adjacency_list[edge[1]-1].add(edge[0])

    return adjacency_list

#Example usage
# if __name__ == "__main__":
#     n = 6  # Number of vertices
#     random_graph = generate_random_graph(n)
#     print("Random Graph Adjacency List:", random_graph)



def generate_set_system_from_graph_adjacency_list(graph): 
    return null

def generate_set_system_from_graph_adjacency_matrix(graph):
    return null