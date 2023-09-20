"""
    Programa:
    Algoritmo de hash para un string
    
    Autores: 
    Santiago Rodriguez
    Juan Pablo Cabrera
    David Langarica Hernandez
    
    Fecha: 
    19/09/2023
    
    Descripcion:
    El programa recibe un archivo de texto y 
    genera un hash de 256 bits a partir de este.
"""

# Imports
import os
import math


# Abrir archivo de texto desde la carpeta del programa
# Complejidad: O(1)
def open_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, "r") as file:
        content = file.read()
    return content


# Pedir al usuario un multiplo de 4 entre 16 y 64
# Complejidad: O(1)
def get_n():
    while True:
        n = int(input("Ingrese un multiplo 'n' de 4 entre 16 y 64: "))
        if n in range(16, 65) and n % 4 == 0:
            break
    return n


# Generar matriz a partir del archivo de texto
# Complejidad: O(n^2)
def generar_matriz(file, n):
    num_filas = math.ceil(len(file) / n)
    matriz = [[0] * n for _ in range(num_filas)]

    # Add file content to matriz
    count = 0
    for i in range(num_filas):
        for j in range(n):
            if count >= len(file):
                matriz[i][j] = "["
            elif file[count] == "\n":
                matriz[i][j] = "-"
            else:
                matriz[i][j] = file[count]
            count += 1

    return matriz


# Imprimir matriz
# Complejidad: O(n^2)
def imprimir_matriz(matriz):
    print(
        "\nMatriz generada por el algoritmo, los saltos de linea se representan con '-' y los espacios con '[':\n"
    )
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()
    print("\n")


# Sumar los valores ascii de cada columna
# Complejidad: O(n^2)
def suma_ascii(matriz):
    # Retorna una lista con la suma de los valores ascii de cada columna
    suma = []
    for j in range(len(matriz[0])):
        suma_col = 0
        for i in range(len(matriz)):
            if matriz[i][j] == "-":
                suma_col += 10
            elif matriz[i][j] == "[":
                suma_col += 16
            else:
                suma_col += ord(matriz[i][j])
        suma.append(suma_col)
    return suma


# Aplicar hash 256 a cada columna
# Complejidad: O(n)
def hash256(suma_ascii):
    # Retorna una matriz con hash 256 de cada columna
    hash256 = []
    for i in range(len(suma_ascii)):
        hash256.append(suma_ascii[i] % 256)
    return hash256


# Convertir a hexadecimal
# Complejidad: O(n)
def toHex(hash256):
    # Retorna una matriz con hash 256 de cada columna
    toHex = []
    for i in range(len(hash256)):
        res = hex(hash256[i])[2:].upper()
        toHex.append(res)
    return toHex


# Concatenar de n en n
# Complejidad: O(n)
def concat(n, toHex):
    n = n // 4
    string = "".join([str(elem) for elem in toHex])

    # Concatenar de n en n
    # Si no hay n caracteres para concatenar, se rellena con 0
    res = []
    for i in range(0, len(string), n):
        if i + n > len(string):
            res.append(string[i : len(string)] + "0" * (n - (len(string) - i)))
        else:
            res.append(string[i : i + n])
    res = " ".join([str(elem) for elem in res])
    return res


if __name__ == "__main__":
    file_name = input("Ingrese el nombre del archivo de texto (sin extension): ")
    file = open_file(file_name + ".txt")
    n = get_n()
    matriz = generar_matriz(file, n)
    imprimir_matriz(matriz)
    suma_ascii = suma_ascii(matriz)
    print("Matriz con suma de valores por columna:\n", suma_ascii, "\n")
    hash256 = hash256(suma_ascii)
    print("Matriz con hash 256 por columna:\n", hash256, "\n")
    toHex = toHex(hash256)
    print("Matriz con hash 256 en hexadecimal por columna:\n", toHex, "\n")
    res = concat(n, toHex)
    print("Representacion hexadecimal:\n", res, "\n")
