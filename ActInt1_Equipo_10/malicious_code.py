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