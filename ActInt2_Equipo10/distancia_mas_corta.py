import math


def calcular_distancia(punto1, punto2):
    """Calcula la distancia euclidiana entre dos puntos."""
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)


def encontrar_central_mas_cercana(centrales, nueva_central):
    """Encuentra la central más cercana a la nueva ubicación, con coordenadas hardcodeadas."""
    distancia_minima = float("inf")
    central_mas_cercana = None

    for central in centrales:
        distancia = calcular_distancia(central, nueva_central)
        if distancia < distancia_minima:
            distancia_minima = distancia
            central_mas_cercana = central

    return central_mas_cercana, distancia_minima
