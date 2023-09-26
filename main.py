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
import math


# Abrir archivo de texto desde la carpeta del programa
# Complejidad: O(1)
def open_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, "r") as file:
        content = file.read()
    return content
