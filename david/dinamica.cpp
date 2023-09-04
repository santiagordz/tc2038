#include <algorithm>
#include <iostream>
#include <vector>

// La complejidad de este algoritmo es O(N*C) donde N es la cantidad de monedas y C es el cambio a dar.

void imprimirNumMonedas(std::vector<int> &monedas, int cambio, int N, int **cambioMatriz) {
    std::vector<std::pair<int, int>> monedasPair;
    int M = N - 1;
    int Cant = cambio;

    for (int i = 0; i < N; i++) {
        monedasPair.push_back(std::make_pair(monedas[i], 0));
    }

    while (M >= 0 && Cant > 0) {
        if (M == 0) {
            monedasPair[M].second = Cant;
            Cant = 0;
        } else if (cambioMatriz[M][Cant] == cambioMatriz[M - 1][Cant]) {
            M--;
        } else {
            monedasPair[M].second++;
            Cant -= monedas[M];
        }
    }

    for (int i = N - 1; i >= 0; i--) {
        std::cout << monedasPair[i].second << std::endl;
    }
}

void darCambio(std::vector<int> &monedas, int cambio) {
    std::sort(monedas.begin(), monedas.end());
    int N = monedas.size();

    int **cambioMatriz = new int *[N + 1];

    for (int i = 0; i <= N; i++) {
        cambioMatriz[i] = new int[cambio + 1];
    }

    for (int i = 0; i < N; i++) {
        cambioMatriz[i][0] = 0;
    }

    for (int n = 0; n < N; n++) {
        for (int c = 1; c <= cambio; c++) {
            if (n == 0) {
                cambioMatriz[n][c] = 1 + cambioMatriz[n][c - monedas[0]];
            } else if (c < monedas[n]) {
                cambioMatriz[n][c] = cambioMatriz[n - 1][c];
            } else {
                cambioMatriz[n][c] = std::min(cambioMatriz[n - 1][c], 1 + cambioMatriz[n][c - monedas[n]]);
            }
        }
    }

    imprimirNumMonedas(monedas, cambio, N, cambioMatriz);

    for (int i = 0; i <= N; i++) {
        delete[] cambioMatriz[i];
    }
    delete[] cambioMatriz;
}

int main() {
    std::cout << "Prueba 1" << std::endl;
    std::vector<int> monedas_1 = {5, 25, 10, 50};
    int P_1 = 325;
    int Q_1 = 500;
    int cambioNecesario_1 = Q_1 - P_1;

    darCambio(monedas_1, cambioNecesario_1);

    std::cout << "Prueba 2" << std::endl;
    std::vector<int> monedas_2 = {20, 25, 10, 5};
    int P_2 = 160;
    int Q_2 = 200;
    int cambioNecesario_2 = Q_2 - P_2;

    darCambio(monedas_2, cambioNecesario_2);

    std::cout << "Prueba 3" << std::endl;
    std::vector<int> monedas_3 = {1, 10, 7};
    int P_3 = 85;
    int Q_3 = 100;
    int cambioNecesario_3 = Q_3 - P_3;

    darCambio(monedas_3, cambioNecesario_3);

    std::cout << "Prueba 4" << std::endl;
    std::vector<int> monedas_4 = {100, 25, 10, 5, 1};
    int P_4 = 711;
    int Q_4 = 1000;
    int cambioNecesario_4 = Q_4 - P_4;

    darCambio(monedas_4, cambioNecesario_4);

    return 0;
}