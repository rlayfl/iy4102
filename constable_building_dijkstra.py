# If you spent the whole lesson playing games, scrolling through Instagram or asleep, this is for you:

# For this assignment, your task is to implement the algorithm for Constable Building.

# You can think of nodes as rooms or other points of interest in the building such as reception, the vending machine or the water fountain.
# You can think of vertices as the paths between the rooms or points of interest such as corridors.
# The coding part is reasonably straightforward, especially given the content available for it online. However, what I am interested in is whether you understand how this applies to a real situation.

# This is also a great opportunity to get to grips with numpy which is used for advanced calculations: https://numpy.org/
import numpy as np


# This adjacency matrix represents a graph with 5 nodes and 7 edges, or, in practical terms, 5 points of interest in Constable Building and 7 corridors connecting them.

adj_matrix = np.array([
    #  A   B   C   D   E
    [  0, 10,  3,  0,  0],  # A → B (10), A → C (3)
    [  0,  0,  1,  2,  0],  # B → C (1), B → D (2)
    [  0,  4,  0,  8,  2],  # C → B (4), C → D (8), C → E (2)
    [  0,  0,  0,  0,  7],  # D → E (7)
    [  0,  0,  0,  9,  0]   # E → D (9)
])

# If A was reception and B was the vending machine, the cost to reach it would be 1. If C was CB12, the cost to reach it would be 3. A cost of 0 implies that there is no path connecting the two points.

# Calculate the number of edges
num_edges = np.count_nonzero(adj_matrix)
print(f"Number of edges: {num_edges}")

start_node = 0

def dijkstra(adj_matrix, start):
    num_nodes = len(adj_matrix)
    distances = [float('inf')] * num_nodes  # Store shortest distance to each node
    distances[start] = 0  # Distance to start node is 0
    visited = [False] * num_nodes  # Track visited nodes
    
    for _ in range(num_nodes):
        # Select the unvisited node with the smallest distance
        min_distance = float('inf')
        min_index = -1
        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i
        
        # Mark the selected node as visited
        visited[min_index] = True
        
        # Update distances for adjacent nodes
        for neighbour in range(num_nodes):
            edge_weight = adj_matrix[min_index][neighbour]
            if edge_weight > 0 and not visited[neighbour]:  # Check for edge existence
                new_distance = distances[min_index] + edge_weight
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance

    return distances

def begin_dijkstras(adj_matrix, start_node):
    shortest_distances = dijkstra(adj_matrix, start_node)
    print(f"Shortest distances from node {start_node}: {shortest_distances}")

# Start software
begin_dijkstras(adj_matrix, start_node)
