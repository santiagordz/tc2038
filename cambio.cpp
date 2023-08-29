#include <iostream>
#include <vector>

using namespace std;

int cambio(int cambio, vector<int> &monedas)
{
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
    return matriz[rows - 1][cambio];
}

int main()
{
    vector<int> monedas = {3};
    int change = 2;
    cout << cambio(change, monedas);
}