#include <algorithm>
#include <iostream>
#include <vector>

// La complejidad de este algoritmo es O(N log N) donde N es la cantidad de monedas.

void darCambio(std::vector<int> &monedas, int cambio) {
    std::sort(monedas.begin(), monedas.end());

    int N = monedas.size();

    std::vector<std::pair<int, int>> monedasNecesarias = {};
    int suma = 0;

    for (int i = 0; i < N; i++) {
        monedasNecesarias.push_back(std::make_pair(monedas[i], 0));
    }

    for (int i = N - 1; i >= 0; i--) {
        while (suma + monedas[i] <= cambio) {
            suma += monedas[i];
            monedasNecesarias[i].second++;
        }
    }

    for (int i = N - 1; i >= 0; i--) {
        std::cout << monedasNecesarias[i].second << std::endl;
    }
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