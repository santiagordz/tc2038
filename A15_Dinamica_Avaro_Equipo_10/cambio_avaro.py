"""
    Equipo 10
    Ejemplo de cambio avaro
    Complejidad: O(n log n)
"""


def darCambio(num_moneda, monedas, costo, pago):
    cambio = pago - costo  # Calcula el cambio a dar
    monedas.sort(reverse=True)  # Ordena las monedas de mayor a menor
    monedasUsadas = []  # Lista de monedas a dar de cambio
    for moneda in monedas:  # Recorre las monedas
        while cambio >= moneda:  # Mientras el cambio sea mayor o igual a la moneda
            cambio -= moneda  # Resta la moneda al cambio
            monedasUsadas.append(moneda)  # Agrega la moneda
    return monedasUsadas  # Regresa la lista de monedas a dar de cambio


print("Caso de prueba 1: ")
print(darCambio(4, [5, 25, 10, 50], 325, 500))

print("Caso de prueba 2: ")
print(darCambio(4, [20, 25, 10, 5], 160, 200))

print("Caso de prueba 3: ")
print(darCambio(3, [1, 10, 7], 85, 100))

print("Caso de prueba 4: ")
print(darCambio(5, [100, 25, 10, 5, 1], 100, 711))
