"""
Autores: David Langarica, Santiago Rodriguez, Juan Pablo Cabrera
Fecha: 8/11/2023
Descripcion: Este programa soluciona el problema de coloreo de grafos
"""

from matrices_test import (
    matriz_prueba_1,
    matriz_prueba_2,
    matriz_prueba_3,
    matriz_prueba_4,
)


def leerMatriz():
    """
    Función para leer la matriz de adyacencias del grafo

    @complexity: O(n^2), donde n es el número de nodos del grafo
    @return: una lista de listas que representa la matriz de adyacencias
    """
    try:
        n = int(input("Ingrese el número de nodos: "))
    except ValueError:
        print("El valor ingresado no es un número entero. Intente nuevamente.")
    matriz = []

    print("Ingrese los valores de la matriz de adyacencias:")
    for _ in range(n):
        fila = list(map(int, input().split()))
        assert (
            len(fila) == n
        ), "La fila debe tener el mismo número de elementos que el número de nodos"
        matriz.append(fila)
    return matriz


def ordenar_vertices(matriz):
    """
    Función para ordenar los vértices de un grafo por grado decreciente según su grado

    @param matriz: una lista de listas que representa la matriz de adyacencias del grafo
    @complexity: O(n^2), donde n es el número de nodos del grafo
    @return: una lista de vértices ordenados por grado decreciente
    """
    n = len(matriz)
    grados = []
    for i in range(n):
        grado = sum(matriz[i])
        grados.append((i, grado))
    grados.sort(key=lambda x: x[1], reverse=True)
    vertices = [x[0] for x in grados]
    return vertices


def colorear(matriz):
    """
    Función para asignar colores a los vértices de un grafo usando el algoritmo de Welsh-Powell

    @param matriz: una lista de listas que representa la matriz de adyacencias del grafo
    @complexity: O(n^2), donde n es el número de nodos del grafo
    @return: una lista de colores asignados a cada vértice
    """
    n = len(matriz)
    vertices = ordenar_vertices(matriz)

    colores = [-1] * n
    color_actual = 0
    colores[vertices[0]] = color_actual
    vertices_coloreados = 1

    while vertices_coloreados < n:
        for i in range(1, n):
            if colores[vertices[i]] == -1:
                if not any(
                    matriz[vertices[i]][vertices[j]]
                    and colores[vertices[j]] == color_actual
                    for j in range(i)
                ):
                    colores[vertices[i]] = color_actual
                    vertices_coloreados += 1
        color_actual += 1

    return colores, vertices_coloreados


def imprimir_resultado(matriz):
    """
    Función para imprimir el resultado del coloreo de un grafo

    @param matriz: una lista de listas que representa la matriz de adyacencias del grafo
    @complexity: O(n), donde n es el número de nodos del grafo
    @return: None
    """
    colores, vertices_coloreados = colorear(matriz)
    if vertices_coloreados == len(matriz):
        for i in range(len(colores)):
            print(f"Vértice: {i}, Color asignado: {colores[i]}")
    else:
        print("No es posible asignar colores a los nodos")


def main():
    print("\n1. Caso de prueba 1")
    imprimir_resultado(matriz_prueba_1)

    print("\n2. Caso de prueba 2")
    imprimir_resultado(matriz_prueba_2)

    print("\n3. Caso de prueba 3")
    imprimir_resultado(matriz_prueba_3)

    print("\n4. Caso de prueba 4")
    imprimir_resultado(matriz_prueba_4)

    print("\n5. Caso de prueba Usuario")
    matriz_prueba_usuario = leerMatriz()
    imprimir_resultado(matriz_prueba_usuario)


if __name__ == "__main__":
    main()
