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