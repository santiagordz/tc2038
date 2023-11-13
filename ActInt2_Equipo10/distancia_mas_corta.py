import math


def calcular_distancia(punto1, punto2):
    """
    Calculates the Euclidean distance between two points in a 2D plane.

    Parameters:
    -----------
    punto1 : tuple
        A point in the 2D plane, represented as a tuple (x1, y1).
    punto2 : tuple
        Another point in the 2D plane, represented as a tuple (x2, y2).

    Complexity:
    ------------
    O(1), as the operation consists of a direct arithmetic calculation.

    Returns:
    --------
    float
        The Euclidean distance between the two given points.

    Example:
    --------
    >>> calcular_distancia((1, 2), (4, 6))
    5.0
    """
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)


def encontrar_central_mas_cercana(centrales, nueva_central):
    """
    Finds the closest central to a given new location.

    Parameters:
    -----------
    centrales : list of tuples
        A list of tuples, where each tuple represents the coordinates (x, y) of an existing central.
    nueva_central : tuple
        The coordinates (x, y) of the new location for which the closest central is sought.

    Complexity:
    ------------
    O(n), where n is the number of centrals in the list. Each central is compared exactly once.

    Returns:
    ---------
    tuple, float
        The tuple represents the coordinates of the closest central, and the float is the distance to that central.

    Example:
    --------
    >>> centrales = [(200, 500), (300, 100), (450, 150)]
    >>> nueva_central = (325, 200)
    >>> encontrar_central_mas_cercana(centrales, nueva_central)
    ((300, 100), 141.4213562373095)
    """
    distancia_minima = float("inf")
    central_mas_cercana = None

    for central in centrales:
        distancia = calcular_distancia(central, nueva_central)
        if distancia < distancia_minima:
            distancia_minima = distancia
            central_mas_cercana = central

    return central_mas_cercana, distancia_minima
