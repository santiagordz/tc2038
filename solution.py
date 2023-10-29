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
