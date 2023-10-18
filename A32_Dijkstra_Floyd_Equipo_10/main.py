"""@package main
Autores: David Langarica, Santiago Rodriguez, Juan Pablo Cabrera
Fecha: 21/10/2023
Descripcion: Este programa implementa los algoritmos de Dijkstra y Floyd para encontrar la distancia más corta entre parejas de nodos en un grafo dirigido.
"""

import copy

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
    assert len(fila) == n, "La fila debe tener el mismo número de elementos que el número de nodos"
    matriz.append(fila)
  return matriz

def dijkstra(matriz, origen):
  """
  Función para implementar el algoritmo de Dijkstra
  
  @complexity: O(n^2), donde n es el número de nodos del grafo
  @param: matriz - una lista de listas que representa la matriz de adyacencias del grafo, origen - un entero que representa el nodo de origen
  @return: una lista que contiene las distancias mínimas desde el origen a todos los demás nodos
  """
  n = len(matriz)
  dist = [float('inf')] * n 
  visitado = [False] * n
  dist[origen] = 0 
  
  for i in range(n): 
    u = minDistancia(dist, visitado) 
    visitado[u] = True 
    for v in range(n):
      if matriz[u][v] != -1 and not visitado[v] and dist[v] > dist[u] + matriz[u][v]: 
        dist[v] = dist[u] + matriz[u][v] 
  return dist

def minDistancia(dist, visitado):
  """
  Función auxiliar para encontrar el nodo no visitado con la distancia mínima desde el origen
  
  @complexity: O(n), donde n es el número de nodos del grafo
  @param: dist - una lista que contiene las distancias desde el origen, visitado - una lista que marca los nodos visitados
  @return: un entero que representa el índice del nodo con la distancia mínima desde el origen
  """
  min = float('inf')
  minIndex = -1
  
  for i in range(len(dist)):
    if not visitado[i] and dist[i] < min: 
      min = dist[i] 
      minIndex = i
  return minIndex

def floyd(matriz):
  """
  Función para implementar el algoritmo de Floyd
  
  @complexity: O(n^3), donde n es el número de nodos del grafo
  @param: matriz - una lista de listas que representa la matriz de adyacencias del grafo
  @return: una lista de listas que contiene las distancias mínimas entre todos los pares de nodos
  """
  n = len(matriz) 
  dist = copy.deepcopy(matriz)
   
  for k in range(n): 
    for i in range(n):
      for j in range(n):
        if dist[i][k] != -1 and dist[k][j] != -1 and (dist[i][j] == -1 or dist[i][j] > dist[i][k] + dist[k][j]):
          dist[i][j] = dist[i][k] + dist[k][j] 
  return dist

if __name__ == "__main__":
  matriz = leerMatriz() 
  
  print()
  print("Dijkstra:") 
  for i in range(len(matriz)):
    dist = dijkstra(matriz, i)
    for j in range(len(matriz)): 
      if i != j: 
        print(f"node {i+1} to node {j+1}: ", end="")
        if dist[j] == float('inf'): 
            print("No hay camino")
        else: 
            print(dist[j])
    print()
        
  print("Floyd:")
  dist = floyd(matriz)
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      print(dist[i][j], end=" ")
    print()
