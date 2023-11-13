from file_operations import build_adjacency_matrix_from_file_lines, open_file
from forma_optima import *
from tsp import slime_mold
from distancia_mas_corta import encontrar_central_mas_cercana


def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()

    n = int(lineas[0].strip())
    matriz_distancias = [list(map(int, line.strip().split()))
                         for line in lineas[1:n+1]]
    matriz_capacidades = [list(map(int, line.strip().split()))
                          for line in lineas[n+1:2*n+1]]
    ubicaciones = [tuple(map(int, line.strip().strip('()').split(',')))
                   for line in lineas[2*n+1:]]

    return matriz_distancias, matriz_capacidades, ubicaciones


# Leer el archivo de entrada
matriz_distancias, matriz_capacidades, ubicaciones = leer_archivo(
    "entrada1.txt")

# Problema 2: Camino más corto (TSP)
route, distance = slime_mold(matriz_distancias)
print("Problema 2")
print(f"Camino más corto: {route}")
print(f"Distancia: {distance} km", end="\n\n")

# Problema 3: Árbol de expansión mínima
msp = min_span_tree(matriz_distancias)
print("Problema 3")
print(msp)

# Problema 4: Central más cercana
centrales = ubicaciones[:-1]
nueva_central = ubicaciones[-1]
central_cercana, distancia = encontrar_central_mas_cercana(
    centrales, nueva_central)
print("Problema 4")
print(f"Central más cercana: {central_cercana}")
print(f"Distancia: {distancia} unidades", end="\n\n")
