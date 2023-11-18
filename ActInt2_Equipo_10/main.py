from file_operations import build_adjacency_matrix_from_file_lines, open_file
from forma_optima import *
from flujo_maximo import *
from tsp import slime_mold, print_route
from distancia_mas_corta import encontrar_central_mas_cercana

NUM_FILES = 3
centrales = None
nueva_central = None

if __name__ == "__main__":
    for i in range(NUM_FILES):
        print(f"Caso de prueba {i+1}", end="\n\n")

        file_structure = open_file(f"Equipo_10_Entrada_{i+1}.txt")
        file_line = file_structure[1]
        adj_matrix = build_adjacency_matrix_from_file_lines(file_line)
        route, distance = slime_mold(adj_matrix)

        print("Problema 2")
        print_route(route, distance)

        print("Problema 3")
        max_flox_matrix = build_adjacency_matrix_from_file_lines(file_structure[2])
        max_flow = ford_fulkerson(max_flox_matrix)
        print(f"El flujo máximo es {max_flow} unidades.", end="\n\n")

        print("Problema 4")
        msp = min_span_tree(adj_matrix)
        print(msp)
        centrales = file_structure[3]
        nueva_central = file_structure[4][0]
        central_cercana, distancia = encontrar_central_mas_cercana(
            centrales, nueva_central
        )
        print(
            f"La central más cercana es {central_cercana} con una distancia de {distancia} unidades."
        )

        print()
        print()
