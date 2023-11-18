import os
import numpy as np


def open_file(file_name):
    """
    Opens a text file from the program's folder.

    Parameters:
    -----------
    file_name : str
        The name of the file to open.

    Returns:
    --------
    list
        A list of lists, where each list represents a line of the file.
    """
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
    """
    Builds an adjacency matrix from a list of lists representing the lines of a file.

    Parameters:
    -----------
    file_line : list
        A list of lists, where each list represents a line of the file.

    Returns:
    --------
    numpy array
        A numpy array representing the adjacency matrix.
    """
    adjacency_matrix = np.array(file_line)
    return adjacency_matrix
