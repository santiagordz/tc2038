#include <iostream>
#include <vector>

/*
 * Problema Rata en un laberinto
 * Equipo 10
 * Algoritmo Backtracking
 * Criterio de avance: La rata solo puede avanzar hacia frente o hacia abajo
 * Complejidad: O(M*C) donde M es el número de filas y C es el número de columnas
 */

void imprimirSolucion(int** solucion, int M, int C) {
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < C; j++) {
            std::cout << solucion[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

bool esLugarValido(int x, int y, std::vector<std::vector<int>>& laberinto, int M, int C) {
    if (x >= 0 && x < M && y >= 0 && y < C && laberinto[x][y] == 1) {
        return true;
    }
    return false;
}

bool solucionLaberinto(int** solucion, int x, int y, std::vector<std::vector<int>>& laberinto, int M, int C) {
    if (x == M - 1 && y == C - 1) {
        solucion[x][y] = 1;
        return true;
    }

    if (esLugarValido(x, y, laberinto, M, C)) {
        solucion[x][y] = 1;

        if (solucionLaberinto(solucion, x + 1, y, laberinto, M, C)) {
            return true;
        }

        if (solucionLaberinto(solucion, x, y + 1, laberinto, M, C)) {
            return true;
        }

        solucion[x][y] = 0;
        return false;
    }

    return false;
}

void calcularCamino(std::vector<std::vector<int>>& laberinto, int M, int C) {
    int** solucion = new int*[M];
    for (int i = 0; i <= M; i++) {
        solucion[i] = new int[C];
        for (int j = 0; j <= C; j++) {
            solucion[i][j] = 0;
        }
    }

    solucionLaberinto(solucion, 0, 0, laberinto, M, C);
    imprimirSolucion(solucion, M, C);

    for (int i = 0; i <= M; i++) {
        delete[] solucion[i];
    }
    delete[] solucion;
}

int main() {
    std::cout << std::endl
              << "Prueba 1" << std::endl;
    int M_1 = 4;
    int C_1 = 4;
    std::vector<std::vector<int>> laberinto_1 = {{1, 0, 0, 0},
                                                 {1, 1, 0, 1},
                                                 {0, 1, 0, 0},
                                                 {1, 1, 1, 1}};
    calcularCamino(laberinto_1, M_1, C_1);

    std::cout << std::endl
              << "Prueba 2" << std::endl;
    int M_2 = 4;
    int C_2 = 5;
    std::vector<std::vector<int>> laberinto_2 = {{1, 0, 1, 1, 1},
                                                 {1, 1, 1, 0, 1},
                                                 {1, 0, 1, 1, 1},
                                                 {1, 1, 1, 0, 1}};
    calcularCamino(laberinto_2, M_2, C_2);

    std::cout << std::endl
              << "Prueba 3" << std::endl;
    int M_3 = 7;
    int C_3 = 9;
    std::vector<std::vector<int>> laberinto_3 = {{1, 1, 0, 1, 1, 1, 1, 1, 0},
                                                 {0, 1, 1, 1, 0, 0, 0, 1, 1},
                                                 {1, 1, 0, 1, 1, 1, 1, 1, 0},
                                                 {1, 0, 0, 0, 1, 1, 0, 1, 1},
                                                 {1, 1, 0, 1, 1, 0, 0, 0, 1},
                                                 {0, 1, 0, 1, 0, 1, 0, 0, 1},
                                                 {1, 1, 1, 1, 0, 1, 1, 0, 1}};
    calcularCamino(laberinto_3, M_3, C_3);

    return 0;
}
