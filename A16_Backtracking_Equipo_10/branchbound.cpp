#include <iostream>
#include <queue>
#include <vector>

/*
 * Problema Rata en un laberinto
 * Equipo 10
 * Algoritmo Branch and Bound
 * Criterio de avance: La rata solo puede avanzar hacia frente o hacia abajo
 */

struct Nodo {
    int x;
    int y;
    int distancia;
    Nodo(int x, int y, int distancia) : x(x), y(y), distancia(distancia) {}
};

struct CompararNodos {
    bool operator()(Nodo const& nodoA, Nodo const& nodoB) {
        return nodoA.distancia > nodoB.distancia;
    }
};

void imprimirSolucion(int** solucion, int M, int C) {
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < C; j++) {
            std::cout << solucion[i][j] << " ";
        }
        std::cout << std::endl;
    }

    for (int i = 0; i <= M; i++) {
        delete[] solucion[i];
    }
    delete[] solucion;
}

void calcularCamino(std::vector<std::vector<int>>& laberinto, int M, int C) {
    int** solucion = new int*[M];
    for (int i = 0; i <= M; i++) {
        solucion[i] = new int[C];
        for (int j = 0; j <= C; j++) {
            solucion[i][j] = 0;
        }
    }
    std::priority_queue<Nodo, std::vector<Nodo>, CompararNodos> colaPriorizada;
    colaPriorizada.push(Nodo(0, 0, 0));

    std::vector<Nodo> mejorSolucion;
    std::vector<Nodo> solucionActual;

    while (!colaPriorizada.empty()) {
        Nodo nodoActual = colaPriorizada.top();
        colaPriorizada.pop();

        int x = nodoActual.x;
        int y = nodoActual.y;
        int distancia = nodoActual.distancia;

        if (x == M - 1 && y == C - 1) {
            return;
        }

        if (x == 0 && y == 0) {
            solucionActual.push_back(nodoActual);
            mejorSolucion = solucionActual;
            colaPriorizada.push(Nodo(x + 1, y, distancia + 1));
            colaPriorizada.push(Nodo(x, y + 1, distancia + 1));
        } else if (x < M && y < C && laberinto[x][y] == 1) {
            
        }
    }

    for (int i = 0; i < mejorSolucion.size(); i++) {
        solucion[mejorSolucion[i].x][mejorSolucion[i].y] = 1;
    }

    imprimirSolucion(solucion, M, C);
}

int main() {
    // std::cout << std::endl
    //           << "Prueba 1" << std::endl;
    // int M_1 = 4;
    // int C_1 = 4;
    // std::vector<std::vector<int>> laberinto_1 = {{1, 0, 0, 0},
    //                                              {1, 1, 0, 1},
    //                                              {0, 1, 0, 0},
    //                                              {1, 1, 1, 1}};
    // calcularCamino(laberinto_1, M_1, C_1);

    // std::cout << std::endl
    //           << "Prueba 2" << std::endl;
    // int M_2 = 4;
    // int C_2 = 5;
    // std::vector<std::vector<int>> laberinto_2 = {{1, 0, 1, 1, 1},
    //                                              {1, 1, 1, 0, 1},
    //                                              {1, 0, 1, 1, 1},
    //                                              {1, 1, 1, 0, 1}};
    // calcularCamino(laberinto_2, M_2, C_2);

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
