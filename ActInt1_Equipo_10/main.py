"""
    Programa:
    Actividad Integradora 1
    
    Autores: 
    Santiago Rodriguez
    Juan Pablo Cabrera
    David Langarica Hernandez
    
    Fecha: 
    01/10/2023
    
    Descripcion:
    El proyecto consiste en desarrollar un programa que realiza varias tareas de análisis en archivos de texto.
    A continuación, se presenta un resumen de las principales funcionalidades del programa:

    Comparación de Códigos Maliciosos:
    El programa verifica si el contenido de los archivos mcode1 está contenido en los archivos transmission
    Devuelve "true" seguido de la posición en el archivo de transmisión donde inicia el código malicioso.
    
    Detección de Palíndromos:
    El programa busca códigos palindromos dentro de los archivos de transmisión.
    Muestra la posición de inicio y finalización del palíndromo más largo en cada archivo de transmisión.
    
    Comparación de Archivos de Transmisión:
    Analiza la similitud entre los archivos de transmisión.
    Muestra la posición inicial y final del primer substring más largo común.
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


# ------------------------------ 1. Comparación de Códigos Maliciosos ------------------------------
# Construye un suffix array para un texto dado.
# Complejidad: O(n log n)
def build_suffix_array(text):
    # Crea una lista de tuplas
    suffixes = [(text[i:], i) for i in range(len(text))]
    # Ordena los sufijos
    suffixes.sort()
    # Extrae las posiciones iniciales ordenadas.
    suffix_array = [suffix[1] for suffix in suffixes]

    return suffix_array


# Busca el mcode en el archivo de transmisión.
# Complejidad: O(n)
def search_substring(text, substring):
    suffix_array = build_suffix_array(text)
    positions = []

    # Realiza una búsqueda en el sufijo del texto.
    for suffix_start in suffix_array:
        suffix_end = suffix_start + len(substring)
        # Check if the substring is a prefix of the current suffix.
        if text[suffix_start:suffix_end] == substring:
            # Add the position of the suffix to the list of positions.
            positions.append((suffix_start, suffix_end))

    positions.sort()

    if positions:
        return True, positions
    return False


# Imprime resultados de busqueda de mcode.
# Complejidad: O(1)
def print_mcode_results(results):
    if type(results) == tuple:
        for position in results[1]:
            print(
                "(true) Posicion Inicial:",
                position[0],
                "Posicion Final:",
                position[1],
            )
    else:
        print("(false) Cadena no encontrada en la transmisión")


if __name__ == "__main__":
    print("Archivo de transmisión 1: ")
    transmision1 = open_file("casos-de-prueba/transmission01.txt")
    print(transmision1, "\n")

    print("Archivo de transmisión 2: ")
    transmision2 = open_file("casos-de-prueba/transmission02.txt")
    print(transmision2, "\n")

    print("Archivo de mcode 1: ")
    mcode1 = open_file("casos-de-prueba/mcode01.txt")
    print(mcode1, "\n")

    print("Archivo de mcode 2: ")
    mcode2 = open_file("casos-de-prueba/mcode02.txt")
    print(mcode2, "\n")

    print("Archivo de mcode 3: ")
    mcode3 = open_file("casos-de-prueba/mcode03.txt")
    print(mcode3, "\n")

    print("T R A N S M I S I O N  1\n")
    print("mcode 1:")
    print_mcode_results(search_substring(transmision1, mcode1))
    print("mcode 2:")
    print_mcode_results(search_substring(transmision1, mcode2))
    print("mcode 3:")
    print_mcode_results(search_substring(transmision1, mcode3))

    print("\n\nT R A N S M I S I O N  2\n")
    print("mcode 1:")
    print_mcode_results(search_substring(transmision2, mcode1))
    print("mcode 2:")
    print_mcode_results(search_substring(transmision2, mcode2))
    print("mcode 3:")
    print_mcode_results(search_substring(transmision2, mcode3))
