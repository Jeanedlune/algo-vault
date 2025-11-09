#include <iostream>
#include <vector>
#include <limits>
#include <stdexcept>
using namespace std;

int findMinimum(const vector<int>& arr) {
    if (arr.empty()) {
        throw invalid_argument("Array cannot be empty");
    }
    
    int minVal = arr[0];
    for (int i = 1; i < (int)arr.size(); ++i) {
        if (arr[i] < minVal) {
            minVal = arr[i];
        }
    }
    
    return minVal;
}

int main() {
    // Test cases
    cout << findMinimum({3, 1, 4, 1, 5}) << endl; // 1
    cout << findMinimum({10, 20, 5, 30, 2}) << endl; // 2
    cout << findMinimum({7}) << endl; // 7
    cout << findMinimum({5, 5, 5}) << endl; // 5
    cout << findMinimum({-10, 0, 5, -3}) << endl; // -10
    
    return 0;
}
