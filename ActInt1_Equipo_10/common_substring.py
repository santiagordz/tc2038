# ------------------------------ 3. Sub-String más largo común: ------------------------------
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
# Basado en la propuesta por: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
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