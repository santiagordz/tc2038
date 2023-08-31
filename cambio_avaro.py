def darCambio(num_moneda, monedas, costo, pago):
    cambio = pago - costo
    monedas.sort(reverse=True)
    monedas_usadas = []
    for moneda in monedas:
        while cambio >= moneda:
            cambio -= moneda
            monedas_usadas.append(moneda)
    return monedas_usadas

print("Caso de prueba 1: ")
print(darCambio(4, [5, 25, 10, 50], 325, 500))


print("Caso de prueba 3: ")
print(darCambio(4, [20, 25, 10, 5], 160, 200))

print("Caso de prueba 4: ")
print(darCambio(3, [1, 10, 7], 85, 100))

print("Caso de prueba 5: ")
print(darCambio(3, [100, 25,10,5,1], 100, 711))