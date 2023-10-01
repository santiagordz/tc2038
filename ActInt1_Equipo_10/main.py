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
from file_operations import open_file
from malicious_code import search_substring, print_mcode_results
from palindromes import find_longest_palindrome
from common_substring import find_longest_common_substring, find_substring_positions, print_substring_positions


if __name__ == "__main__":
    # ----------------------- Lectura de archivos -----------------------
    print("Archivo de transmisión 1: ")
    transmission1 = open_file("casos-de-prueba/transmission01.txt")
    print(transmission1, "\n")

    print("Archivo de transmisión 2: ")
    transmission2 = open_file("casos-de-prueba/transmission02.txt")
    print(transmission2, "\n")

    print("Archivo de mcode 1: ")
    mcode1 = open_file("casos-de-prueba/mcode01.txt")
    print(mcode1, "\n")

    print("Archivo de mcode 2: ")
    mcode2 = open_file("casos-de-prueba/mcode02.txt")
    print(mcode2, "\n")

    print("Archivo de mcode 3: ")
    mcode3 = open_file("casos-de-prueba/mcode03.txt")
    print(mcode3, "\n")
    
    # ----------------------- 1. Comparación de Códigos Maliciosos -----------------------
    print("T R A N S M I S S I O N  1\n")
    print("mcode 1:")
    print_mcode_results(search_substring(transmission1, mcode1))
    print("mcode 2:")
    print_mcode_results(search_substring(transmission1, mcode2))
    print("mcode 3:")
    print_mcode_results(search_substring(transmission1, mcode3))

    print("\n\nT R A N S M I S S I O N  2\n")
    print("mcode 1:")
    print_mcode_results(search_substring(transmission2, mcode1))
    print("mcode 2:")
    print_mcode_results(search_substring(transmission2, mcode2))
    print("mcode 3:")
    print_mcode_results(search_substring(transmission2, mcode3))
    
    # ----------------------- 2. Detección de Palíndromos -----------------------
    palindrome1, start1, end1 = find_longest_palindrome(transmission1)
    palindrome2, start2, end2 = find_longest_palindrome(transmission2)


    print("\n\n\nPalíndromo más largo en la transmisión 1:")
    print("Texto del palíndromo:", palindrome1)
    print("Posición Inicial:", start1)
    print("Posición Final:", end1)
    
    print("\nPalíndromo más largo en la transmisión 2:")
    print("Texto del palíndromo:", palindrome2)
    print("Posición Inicial:", start2)
    print("Posición Final:", end2)
    
    # ----------------------- 3. Sub-String más largo común: -----------------------
    common_substring = find_longest_common_substring(transmission1, transmission2)

    if common_substring:
        print("\n\n\nSub-String más largo:", common_substring)
        
        positions_in_transmission1 = find_substring_positions(transmission1, common_substring)
        positions_in_transmission2 = find_substring_positions(transmission2, common_substring)

        print_substring_positions("Transmisión 1", positions_in_transmission1)
        print_substring_positions("Transmisión 2", positions_in_transmission2)

    else:
        print("No se encontró un substring compartido en ambas transmisiones.")
