import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def illustrate_graph_from_adjacency_matrix(adjacency_matrix):
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
