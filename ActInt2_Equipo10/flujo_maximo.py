import numpy as np

def build_adjacency_matrix_from_file_lines(file_line):
    adjacency_matrix = np.array(file_line)
    return adjacency_matrix

# Function to find the maximum flow using Ford-Fulkerson algorithm
def ford_fulkerson(graph):
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
