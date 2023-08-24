#include <vector>
#include <iostream>

using namespace std;

void merge(vector<int>& arr, int s, int m, int e) {
    // Copy the sorted left & right halfs to temp arrays
    vector<int> L = {arr.begin() + s, arr.begin() + m + 1};
    vector<int> R = {arr.begin() + m + 1, arr.begin() + e + 1}; 

    int i = 0; // index for L
    int j = 0; // index for R
    int k = s; // index for arr

    while (i < L.size() && j < R.size()) {
        if (L[i] <= R[j]) {
            arr[k] = L[i++];
        } else {
            arr[k] = R[j++];
        }
        k++;
    }

    // One of the halfs will have elements remaining
    while (i < L.size()) {
        arr[k++] = L[i++];
    }
    while (j < R.size()) {
        arr[k++] = R[j++];
    }
}

vector<int> mergeSort(vector<int>& arr, int s, int e) {
    if (s >= e) {
        return arr;
    }
    // The middle index of the array
    int m = (s + e)  / 2;

    // Sort the left half
    mergeSort(arr, s, m);

    // Sort the right half
    mergeSort(arr, m + 1, e);

    // Merge sorted halfs
    merge(arr, s, m, e);
    
    return arr;
}

int main() {
    vector<int> arr = {5, 4, 3, 2, 1};
    mergeSort(arr, 0, arr.size() - 1);
    // Print
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    return 0;
}