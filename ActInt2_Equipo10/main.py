from file_operations import build_adjacency_matrix_from_file_lines, open_file
from forma_optima import *
from tsp import slime_mold

file_structure = open_file("entrada1.txt")
file_line_1 = file_structure[1]
adj_matrix_1 = build_adjacency_matrix_from_file_lines(file_line_1)

route, distance = slime_mold(adj_matrix_1)

print("Problema 2")
print(f"Camino más corto: {route}")
print(f"Distancia: {distance} km", end="\n\n")

print("Problema 3")
msp = min_span_tree(adj_matrix_1)
print(msp)
