import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def illustrate_graph_from_adjacency_matrix(adjacency_matrix):
    """
    Illustrates a graph from an adjacency matrix using NetworkX and Matplotlib.

    Parameters:
    -----------
    adjacency_matrix : numpy.ndarray
        A 2D numpy array representing the adjacency matrix of the graph. Each element
        (i, j) in the matrix represents the weight of the edge between nodes i and j.

    Description:
    ------------
    This function creates a graph from the given adjacency matrix and displays it. The nodes are
    arranged in a shell layout, and the edges are labeled with their respective weights.

    Notes:
    ------
    - The graph is undirected.
    - Nodes without connections are not displayed.
    - Edge weights are assumed to be non-negative.

    Returns:
    --------
    None
    """
    if adjacency_matrix is not None:
        G = nx.from_numpy_array(adjacency_matrix, create_using=nx.Graph())

        # Use 'shell_layout' for a straight and square layout
        pos = nx.shell_layout(G)

        # Extract edge weights from the adjacency matrix
        edge_labels = {
            (i, j): str(weight)
            for i, row in enumerate(adjacency_matrix)
            for j, weight in enumerate(row)
            if weight != 0
        }

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue")

        # Draw edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph with Edge Weights")
        plt.show()
    else:
        print("Unable to illustrate graph.")


def min_span_tree(adjacency_matrix):
    """
    Computes the minimum spanning tree (MST) of a graph represented by an adjacency matrix.

    Parameters:
    -----------
    adjacency_matrix : numpy.ndarray
        A 2D numpy array where each element (i, j) represents the weight of the edge between
        nodes i and j. A weight of 0 implies no edge between the nodes.

    Description:
    ------------
    This function uses Prim's algorithm to find the MST of the graph. It starts from the first node
    and iteratively adds the shortest edge connecting the tree to a new node, until all nodes are included.

    Complexity:
    -----------
    O(n^2), where n is the number of nodes in the graph. This is due to the nested loop structure.

    Returns:
    --------
    numpy.ndarray
        A 2D numpy array representing the adjacency matrix of the MST. The weights of the edges
        not included in the MST are set to 0.
    """

    num_nodes = len(adjacency_matrix)
    selected_nodes = np.zeros(num_nodes, dtype=bool)
    selected_nodes[0] = True
    mst_edges = np.zeros_like(adjacency_matrix)
    while not np.all(selected_nodes):
        min_edge = float("inf")
        min_start, min_end = -1, -1

        for i, is_selected in enumerate(selected_nodes):
            if not is_selected:
                continue

            for j in range(num_nodes):
                if not selected_nodes[j] and 0 < adjacency_matrix[i][j] < min_edge:
                    min_edge = adjacency_matrix[i][j]
                    min_start, min_end = i, j

        mst_edges[min_start][min_end] = min_edge
        mst_edges[min_end][min_start] = min_edge
        selected_nodes[min_end] = True

    return mst_edges


def illustrate_graph_from_mst(mst_matrix):
    """
    Illustrates a minimum spanning tree (MST) from its adjacency matrix using NetworkX and Matplotlib.

    Parameters:
    -----------
    mst_matrix : numpy.ndarray
        A 2D numpy array representing the adjacency matrix of the MST. Each element (i, j)
        in the matrix represents the weight of the edge between nodes i and j in the MST.

    Description:
    ------------
    This function creates a graph from the given MST matrix and displays it. The nodes are
    arranged in a shell layout, and the edges are labeled with their respective weights.

    Notes:
    ------
    - The graph is undirected.
    - Nodes without connections are not displayed.
    - Edge weights are assumed to be non-negative.

    Returns:
    --------
    None
    """

    if mst_matrix is not None:
        G = nx.from_numpy_array(mst_matrix, create_using=nx.Graph())

        # Use 'shell_layout' for a straight and square layout
        pos = nx.shell_layout(G)

        # Extract edge weights from the adjacency matrix
        edge_labels = {
            (i, j): str(weight)
            for i, row in enumerate(mst_matrix)
            for j, weight in enumerate(row)
            if weight != 0
        }

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="pink")

        # Draw edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph with Edge Weights")
        plt.show()
    else:
        print("Unable to illustrate graph.")
