#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> cambio(int num_monedas, vector<int> &monedas, int p, int q)
{
    sort(monedas.begin(), monedas.end());
    // Hacer Matriz de PD
    int cambio = q - p;
    int const rows = monedas.size();
    vector<vector<int>> matriz(rows, vector<int>(cambio + 1));
    for (int row = 0; row < rows; row++)
    {
        matriz[row][0] = 0;
    }
    for (int row = 0; row < 1; row++)
    {
        for (int column = 1; column < cambio + 1; column++)
        {
            if (column % monedas[row] != 0)
            {
                matriz[row][column] = -1;
            }
            else
            {
                matriz[row][column] = column / monedas[row];
            }
        }
    }
    for (int row = 1; row < rows; row++)
    {
        for (int column = 1; column < cambio + 1; column++)
        {
            if (column < monedas[row])
            {
                matriz[row][column] = matriz[row - 1][column];
            }
            else if (column == monedas[row])
            {
                matriz[row][column] = 1;
            }
            else
            {
                int best = matriz[row][column - monedas[row]];
                if (best == -1)
                {
                    matriz[row][column] = matriz[row - 1][column];
                }
                else
                {
                    if (matriz[row - 1][column] == -1)
                    {
                        matriz[row][column] = 1 + best;
                    }
                    else
                    {
                        matriz[row][column] = min(1 + best, matriz[row - 1][column]);
                    }
                }
            }
        }
    }

    // Retornar numero de monedas
    vector<int> retorno;
    if (num_monedas > 1)
    {
        int Cant = cambio;
        for (int M = num_monedas - 1; M >= 0; M--)
        {
            while (Cant > 0)
            {
                if (M == 0)
                {
                    retorno.push_back(monedas[0]);
                    Cant -= monedas[M];
                    continue;
                }
                else if (matriz[M][Cant] == matriz[M - 1][Cant])
                {
                    break;
                }

                if (matriz[M][Cant] == 1 + matriz[M][Cant - monedas[M]])
                {
                    retorno.push_back(monedas[M]);
                    Cant -= monedas[M];
                }
            }
        }
    }
    else
    {
        int Cant = cambio;
        while (Cant > 0)
        {
            retorno.push_back(monedas[0]);
            Cant--;
        }
    }
    return retorno;
}

int main()
{
    cout << "Caso de prueba 1:" << endl;
    vector<int> monedas = {5, 25, 10, 50};
    vector<int> sol1 = cambio(4, monedas, 325, 500);
    for (int i = 0; i < sol1.size(); i++)
    {
        cout << sol1[i] << " ";
    }
    cout << endl;
    cout << "Caso de prueba 2:" << endl;
    vector<int> monedas2 = {20, 25, 10, 5};
    vector<int> sol2 = cambio(4, monedas2, 160, 200);
    for (int i = 0; i < sol2.size(); i++)
    {
        cout << sol2[i] << " ";
    }
    cout << endl;
    cout << "Caso de prueba 3:" << endl;
    vector<int> monedas3 = {1, 10, 7};
    vector<int> sol3 = cambio(3, monedas3, 85, 100);
    for (int i = 0; i < sol3.size(); i++)
    {
        cout << sol3[i] << " ";
    }
    cout << endl;
    cout << "Caso de prueba 4:" << endl;
    vector<int> monedas4 = {100, 25, 10, 5, 1};
    vector<int> sol4 = cambio(5, monedas4, 100, 711);
    for (int i = 0; i < sol4.size(); i++)
    {
        cout << sol4[i] << " ";
    }
    cout << endl;
}