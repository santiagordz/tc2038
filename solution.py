"""@
Autores: David Langarica, Santiago Rodriguez, Juan Pablo Cabrera
Fecha: 29/10/2023
Descripcion: Este programa implementa el algoritmo de Programación Dinámica para resolver el problema de la mochila (Knapsack problem). 
El algoritmo toma como entrada el número de elementos disponibles, los beneficios asociados a cada elemento, los pesos de cada elemento y la capacidad máxima de la mochila.
Luego, construye una matriz en la que cada celda representa el beneficio máximo que se puede obtener considerando un subconjunto de los elementos y una capacidad de mochila específica. Finalmente, el programa devuelve el beneficio óptimo que se puede obtener y la matriz generada durante el proceso. 
Complejidad logarítmica: O(N*W), donde N es el número de elementos y W es la capacidad máxima de la mochila.
"""

def mochila(N, beneficios, pesos, W):
    # Inicializando la matriz
    matriz = [[0 for x in range(W + 1)] for x in range(N + 1)]

    # Llenando la matriz en forma bottom-up
    for i in range(N + 1):
        for w in range(W + 1):
            # Caso base (sin elementos o capacidad de la mochila = 0)
            if i == 0 or w == 0:
                matriz[i][w] = 0
            # Si el peso del i-ésimo elemento es menor o igual a la capacidad actual de la mochila
            elif pesos[i-1] <= w:
                matriz[i][w] = max(beneficios[i-1] + matriz[i-1][w-pesos[i-1]], matriz[i-1][w])
            # Si el peso del i-ésimo elemento es mayor que la capacidad actual de la mochila
            else:
                matriz[i][w] = matriz[i-1][w]
                
    # Retornar el beneficio óptimo y la matriz generada
    return matriz[N][W], matriz

N = 3
beneficios = [1, 2, 3]
pesos = [4, 5, 1]
W = 4
beneficio_optimo, matriz = mochila(N, beneficios, pesos, W)
print("Beneficio óptimo:", beneficio_optimo)
print("Matriz generada:")
for fila in matriz:
    print(fila)
