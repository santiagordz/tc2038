from file_operations import build_adjacency_matrix_from_file_lines, open_file
from forma_optima import *
from tsp import slime_mold
from distancia_mas_cercana import encontrar_central_mas_cercana

# Código existente para Problema 2 y 3
file_structure = open_file("entrada1.txt")
file_lines = file_structure  # Asumiendo que file_structure es una lista de líneas

# Problema 2 y 3: usar la primera línea para el problema del agente viajero y el árbol de expansión mínima
file_line_1 = file_lines[0]
adj_matrix_1 = build_adjacency_matrix_from_file_lines(file_line_1)

route, distance = slime_mold(adj_matrix_1)

print("Problema 2")
print(f"Camino más corto: {route}")
print(f"Distancia: {distance} km", end="\n\n")

print("Problema 3")
msp = min_span_tree(adj_matrix_1)
print(msp)

# Problema 4: leer las centrales y la nueva ubicación
# Asumiendo que las centrales están en las líneas subsiguientes y la última línea es la nueva ubicación
centrales = [tuple(map(float, line.split(','))) for line in file_lines[1:-1]]
nueva_central = tuple(map(float, file_lines[-1].split(',')))

central_cercana, distancia = encontrar_central_mas_cercana(
    centrales, nueva_central)

print("Problema 4")
print(
    f"La central más cercana está en {central_cercana} a una distancia de {distancia} km")
