# Imports
import math

# Constants
baseRadius = 1 #m
height = 2 #m
bottleCapacity = 350 #ml

# Functions
def calculateNumberSodas(baseRadius, height, bottleCapacity):
    machineVolume = math.pi * (baseRadius ** 2) * height # Volume of the machine
    bottleCapacity = bottleCapacity / 1000 # Convert bottle capacity to liters
    numberSodas = machineVolume / bottleCapacity # Number of sodas that fit in the machine
    numberSodas = round(numberSodas, 2) # Return with 2 decimals
    return numberSodas

# Main
numberSodas = calculateNumberSodas(baseRadius, height, bottleCapacity)
print("The number of sodas that fit in the machine is:", numberSodas, "bottles")