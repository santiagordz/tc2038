import numpy as np


def build_adjacency_matrix_from_file_lines(file_line):
    """
    Constructs an adjacency matrix from a list of file lines.

    Parameters:
    -----------
    file_line : list
        A list where each element is a sublist representing a row in the adjacency matrix.
        Each sublist contains the edge weights to other nodes in the graph.

    Description:
    ------------
    This function converts a list of lists into a numpy array, which represents the adjacency matrix
    of a graph. The adjacency matrix is a 2D representation of a graph where the element at (i, j)
    represents the weight of the edge from node i to node j.

    Returns:
    --------
    numpy.ndarray
        The adjacency matrix represented as a 2D numpy array.
    """
    adjacency_matrix = np.array(file_line)
    return adjacency_matrix


def ford_fulkerson(graph):
    """
    Implements the Ford-Fulkerson algorithm to find the maximum flow in a flow network.

    Parameters:
    -----------
    graph : numpy.ndarray
        A 2D numpy array representing the flow network as an adjacency matrix. Each element (i, j)
        represents the capacity of the edge from node i to node j.

    Description:
    ------------
    The function calculates the maximum flow from the source (first node of the graph) to the sink
    (last node of the graph). It uses breadth-first search (BFS) to find augmenting paths and
    iteratively adds to the flow until no augmenting paths are left.

    Complexity:
    -----------
    O(max_flow * E), where 'max_flow' is the maximum flow in the network and 'E' is the number of edges.
    This is due to the while loop that runs until no more augmenting paths are found, and the BFS inside it.

    Returns:
    --------
    int
        The value of the maximum flow from the source to the sink in the given flow network.
    """

    def bfs(residual_graph, parent):
        visited = set()
        queue = []
        queue.append(source)
        visited.add(source)
        
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(residual_graph[u]):
                if ind not in visited and val > 0:
                    queue.append(ind)
                    visited.add(ind)
                    parent[ind] = u
                    if ind == sink:
                        return True
        return False
    
    num_vertices = len(graph)
    source = 0  # Assuming first index as source
    sink = num_vertices - 1  # Assuming last index as sink
    parent = [-1] * num_vertices
    max_flow = 0
    residual_graph = np.copy(graph)
    
    # Augment the flow while there is a path from source to sink
    while bfs(residual_graph, parent):
        path_flow = float('inf')
        s = sink
        while(s != source):
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        
        # Add path flow to overall flow
        max_flow += path_flow
        v = sink
        while(v != source):
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
    
    return max_flow
