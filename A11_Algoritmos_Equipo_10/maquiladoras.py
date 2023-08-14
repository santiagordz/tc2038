import random
import math

#Método 1
produccion_camisas = [120, 150, 180, 200, 170, 190, 160, 12, 12, 123, 1, 23, 2, 34, 2345, 3, 5, 43, 5, 46, 45, 6, 45, 6, 54, 64, 6, 34, 5, 34, 5, 34, 5, 345, 34, 53, 5, 3, 45, 3453, 4234234]

paso_m1 = 2
iteraciones_m1 = 0

paso_m2 = 2
iteraciones_m2 = 0


for i in range(0, len(produccion_camisas), paso_m1):
    iteraciones_m1 += 1

for i in range(0, len(produccion_camisas), paso_m2):
    iteraciones_m2 += 4


print(f"La maquiladora 1 se tarda: {iteraciones_m1} dias en acabar el pedido")
print(f"La maquiladora 2 se tarda: {iteraciones_m2} dias en acabar el pedido")


numeroCamisas = random.randint(1, 100)

#Método 3

tiempoMaquiladora1 = 5 #Horas
tiempoMaquiladora2 = 3 #Horas

def tiempoTotal(numeroCamisas, tiempoMaquiladora1, tiempoMaquiladora2):
    tiempoTotal = 0
    for i in range(1, numeroCamisas):
        tiempoTotal += tiempoMaquiladora1 + tiempoMaquiladora2
    return tiempoTotal

print(f"Para hacer {numeroCamisas} camisas;")
print(f"El tiempo total es: {tiempoTotal(numeroCamisas, tiempoMaquiladora1, tiempoMaquiladora2)} horas")
