#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> cambio(int num_monedas, vector<int> &monedas, int p, int q)
{
    sort(monedas.begin(), monedas.end());
    // Hacer Matriz de PD
    int cambio = p - q;
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
    vector<int> monedas = {1, 10, 7};
    vector<int> retorno = cambio(monedas.size(), monedas, 100, 85);
    // print retorno
    cout << "[ ";
    for (int i = 0; i < retorno.size(); i++)
    {
        cout << retorno[i] << ", ";
    }
    cout << "]" << endl;
}