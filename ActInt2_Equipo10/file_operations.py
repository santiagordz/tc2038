import os
import numpy as np


# Abrir archivo de texto desde la carpeta del programa
# Complejidad: O(1)
def open_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    arrays = []
    with open(file_path, "r") as file:
        array = []
        for line in file:
            line = line.strip()
            if line == "":
                if array:
                    arrays.append(array)
                    array = []
            else:
                if line.startswith("(") and line.endswith(")"):
                    # Handle lines with tuples
                    values = line[1:-1].split(",")
                    array.append(tuple(map(int, values)))
                else:
                    # Handle regular matrix rows
                    array.append(list(map(int, line.split())))
        if array:
            arrays.append(array)
    return arrays


def build_adjacency_matrix_from_file_lines(file_line):
    adjacency_matrix = np.array(file_line)
    return adjacency_matrix
