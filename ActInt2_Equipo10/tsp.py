import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from utils import DICTIONARY

EVAPORATION_RATE = 0.1
REINFORCEMENT_RATE = 0.1

ITERATIONS = 10


def initialize_pheromones(distances_matrix):
    """
    Initializes the pheromone matrix based on the distances_matrix matrix.

    Complexity:
    -----------
        O(n^2), where n is the number of nodes.

    Returns:
    --------
    pheromones (numpy.ndarray): A matrix with the same shape as distances_matrix, where
        each element is calculated as 1 / distances_matrix if the corresponding element
        in distances_matrix is greater than 0, otherwise it is set to 0.
    """
    # Ignore division by zero errors
    with np.errstate(all="ignore"):
        # The pheromone levels are calculated initially as 1 / distance between nodes or 0 if the distance is 0
        # The less pheromone level, the higher the distance between nodes
        pheromones = np.where(distances_matrix > 0, 1 / distances_matrix, 0)
    return pheromones


def evaporate_pheromones(pheromones):
    """
    Calculates the new pheromone levels after evaporation.

    Complexity:
    -----------
        O(n^2), where n is the number of nodes.

    Args:
    -----
    - pheromones (numpy array): The current pheromone levels.

    Returns:
    --------
    - new_pheromones (numpy array): The updated pheromone levels after evaporation.
    """
    # The new pheromone levels are calculated as the current pheromone levels multiplied by the evaporation rate
    return (1 - EVAPORATION_RATE) * pheromones


def reinforce_pheromones(pheromones, best_route, best_distance):
    """
    Update the pheromone levels on the edges of the graph based on the best route found and its corresponding distance.

    Complexity:
    -----------
        O(n), where n is the number of nodes.

    Args:
    -----
        pheromones (matrix): A matrix representing the pheromone levels on the edges of the graph.
        best_route (list): A list representing the best route found.
        best_distance (float): The distance of the best route found.

    Returns:
    --------
        matrix: Updated pheromone matrix with the pheromone levels on the edges of the graph after reinforcement.
    """
    for i in range(len(best_route) - 1):
        # The increment is calculated as the reinforcement rate divided by the distance of the best route
        increment = REINFORCEMENT_RATE / best_distance
        pheromones[best_route[i], best_route[i + 1]] += increment
    return pheromones


def choose_next_node(pheromones, actual, visited, distances_matrix):
    """
    Calculates the probability of moving to each unvisited node based on the pheromone levels and the distance between nodes.
    Then selects a node randomly based on these probabilities.

    Complexity:
    -----------
        O(n), where n is the number of nodes.

    Args:
    -----
        pheromones (numpy array): A matrix representing the pheromone levels between nodes.
        actual (int): The index of the current node.
        visited (list): A list of indices of the nodes that have been visited.
        alpha (float, optional): The weight for the pheromone levels in the probability calculation. Default is 1.
        beta (float, optional): The weight for the distance between nodes in the probability calculation. Default is 1.

    Returns:
    --------
        int: The index of the next node to visit.
    """
    # Start with an array of zeros with the same length as the pheromone matrix
    probability = np.zeros(len(pheromones))
    for i in range(len(pheromones)):
        # If the node has not been visited, calculate the probability of moving to that node
        if i not in visited:
            probability[i] = pheromones[actual, i] * (1 / distances_matrix[actual, i])
    # Normalize the probability array so that the sum of all probabilities is 1
    probability = probability / np.sum(probability)
    # Choose the next node randomly based on the probability array
    next_node = np.random.choice(len(pheromones), p=probability)
    return next_node


def map_route(route):
    """
    Maps the route from indices to letters.

    Complexity:
    -----------
        O(n), where n is the length of the route.

    Args:
    -----
        route (list): A list of indices representing the route.

    Returns:
    --------
        list: A list of letters representing the route.
    """
    mapped_route = []

    for i in route:
        # We map the index to the corresponding letter
        mapped_route.append(DICTIONARY[i])
    return mapped_route


def slime_mold(distances_matrix):
    """
    Finds the shortest route using the slime mold algorithm.

    Complexity:
    -----------
        O(i * n^2) where i is the number of iterations and n is the number of nodes. This is due to the nested loops over iterations and the nodes in the pheromone matrix.

    Args:
    -----
        distances_matrix (numpy array): A matrix representing the distances between nodes.

    Returns:
    --------
        list: A list of letters representing the best route found.
        float: The distance of the best route found.
    """
    distances_matrix = np.array(distances_matrix)
    pheromones = initialize_pheromones(distances_matrix)
    best_route = []
    best_distance = np.inf

    # We always start at node 0
    initial_node = 0

    # We run the algorithm ITERATIONS times to find the best route
    for _ in range(ITERATIONS):
        visited = [initial_node]

        # We choose the next node until we have visited all nodes
        while len(visited) < len(distances_matrix):
            next_node = choose_next_node(
                pheromones, visited[-1], visited, distances_matrix
            )
            visited.append(next_node)

        # The distance of this route is calculated
        distance = 0
        for i in range(len(visited) - 1):
            distance += distances_matrix[visited[i], visited[i + 1]]

        # The best_route and best_distance are updated if the current route is better
        if distance < best_distance:
            best_distance = distance
            best_route = visited

        # Update pheromones
        # Evaporation means that pheromones are reduced by 10%
        pheromones = evaporate_pheromones(pheromones)
        # Reinforcement means that pheromones are increased by 10% on the edges of the best route
        pheromones = reinforce_pheromones(pheromones, best_route, best_distance)

    # We add the distance between the last node and the first node to complete the cycle
    best_distance += distances_matrix[best_route[-1], best_route[0]]

    # We add the first node to the end of the route to complete the cycle
    best_route.append(best_route[0])

    # We map the route from indices to letters
    mapped_route = map_route(best_route)

    return mapped_route, best_distance


def animate_route(route, distances_matrix):
    """
    Animates the route of the slime mold.

    Complexity:
    -----------
        O(m * n^2) where m is the number of elements in the route and n is the number of nodes. This is due to the updating of the graph for each frame in the animation.

    Args:
    -----
        route (list): A list of indices representing the route.
    """
    fig, ax = plt.subplots()
    G = nx.from_numpy_array(distances_matrix)

    # Map the indices to letters
    G = nx.relabel_nodes(G, DICTIONARY)

    # Get the positions of the nodes
    pos = nx.spring_layout(G)

    def update(num):
        ax.clear()
        # Get the visited nodes up to this point
        visited_nodes = route[: num + 1]

        # Draw all the edges in the graph
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color="grey")

        # Draw all the nodes in the graph
        nx.draw_networkx_nodes(G, pos, node_color="skyblue", ax=ax)

        # Draw the visited nodes in red
        nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color="red", ax=ax)

        # Draw the labels for the nodes and the edges
        nx.draw_networkx_labels(G, pos, ax=ax)
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), ax=ax
        )

        # If we have visited more than one node, draw the edges between them
        if len(visited_nodes) > 1:
            route_edges = list(zip(visited_nodes[:-1], visited_nodes[1:]))
            nx.draw_networkx_edges(
                G, pos, edgelist=route_edges, edge_color="red", width=2, ax=ax
            )

    anim = animation.FuncAnimation(
        fig, update, frames=len(route), interval=900, repeat=True
    )

    return anim
