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
        # Checa si el substring es un prefijo del sufijo actual.
        if text[suffix_start:suffix_end] == substring:
            # Agrega la posición del sufijo a la lista de posiciones.
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

# ------------------------------ 2. Detección de Palíndromos ------------------------------
# Función para encontrar el palíndromo más largo en una cadena
# Complejidad: O(n^2)
def find_longest_palindrome(text):
    n = len(text)
    table = [[0 for x in range(n)] for y in range(n)]
    

    maxLength = 1
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1


    start = 0
    i = 0
    while i < n - 1 :
        if (text[i] == text[i+1]):
            table[i][i+1] = True
            start = i
            maxLength = 2
        i = i + 1

    cl = 3
    while cl <= n :
        i = 0
        while i < (n - cl + 1) :
            j = i + cl - 1
            if (text[i] == text[j] and table[i + 1][j - 1]) :
                table[i][j] = True
                start = i
                maxLength = cl
            i = i + 1
        cl = cl + 1

    return text[start:start + maxLength], start + 1, start + maxLength


# ------------------------------ 3. Sub-String más largo: ------------------------------
# Funcion para encontrar el substring mas largo en dos archivos de texto.
# Complejidad: O(n^2)
def find_longest_common_substring(text1, text2):
    m = len(text1)
    n = len(text2)
    longest_common_substring = ""

    # Crear una tabla para almacenar las longitudes de los substrings comunes
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Iterar a través de los archivos y llenar la tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > len(longest_common_substring):
                    longest_common_substring = text1[i - table[i][j]:i]
            else:
                table[i][j] = 0

    return longest_common_substring

# Funcion para encontrar las posiciones de un substring en un archivo.
# Complejidad: O(n)
def find_substring_positions(file_content, substring):
    positions = []
    M = len(substring)
    N = len(file_content)

    # calcula el arreglo de prefijos mas largos
    lps = [0]*M
    j = 0

    # Preprocesa el patron (substring) para calcular lps[]
    get_LPS_array(substring, M, lps)

    i = 0
    while i < N:
        if substring[j] == file_content[i]:
            i += 1
            j += 1

        if j == M:
            positions.append((i-j, i-1))
            j = lps[j-1]

        elif i < N and substring[j] != file_content[i]:
            # No coinciden los caracteres
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return positions

# Funcion para calcular el arreglo de prefijos mas largos para un substring dado
# Complejidad: O(n)
def get_LPS_array(substring, M, lps):
    length = 0

    lps[0] = 0
    i = 1

    # El ciclo calcula lps[i] para i = 1 a M-1
    while i < M:
        if substring[i]== substring[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # Busca el caracter que no coincide en lps[0..lps[i-1]]
            if length != 0:
                length = lps[length-1]
                
            else:
                lps[i] = 0
                i += 1

# Imprime las posiciones de un substring en un archivo.
# Complejidad: O(n)
def print_substring_positions(file_name, positions):
    print("\nPosiciones en la {}: ".format(file_name))
    for start, end in positions:
        print("Posicion inicial: {} Posicion final: {}".format(start+1, end+1))

if __name__ == "__main__":
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
    
    common_substring = find_longest_common_substring(transmission1, transmission2)

    if common_substring:
        print("\n\n\nSub-String más largo", common_substring)
        
        positions_in_transmission1 = find_substring_positions(transmission1, common_substring)
        positions_in_transmission2 = find_substring_positions(transmission2, common_substring)

        print_substring_positions("Transmisión 1", positions_in_transmission1)
        print_substring_positions("Transmisión 2", positions_in_transmission2)

    else:
        print("No se encontró un substring compartido en ambas transmisiones.")
    

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
