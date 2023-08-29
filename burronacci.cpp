#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int burronaci(int n)
{
    if (n == 0)
        return 1;
    else if (n == 1)
        return 1;
    vector<int> buro(n + 1);
    buro[0] = 1;
    buro[1] = 2;
    for (int i = 2; i < n; i++)
    {
        buro[i] = 2 * buro[i - 1] + buro[i - 2];
    }
    return buro[n - 1];
}

int main()
{
    int n;
    cout << burronaci(5);
    return 0;
}