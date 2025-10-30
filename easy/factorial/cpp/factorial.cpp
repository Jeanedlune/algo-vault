#include <iostream>
using namespace std;

long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    
    long long result = 1;
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int main() {
    // Test Case 1
    cout << "factorial(5) = " << factorial(5) << " (Expected: 120)" << endl;
    
    // Test Case 2
    cout << "factorial(0) = " << factorial(0) << " (Expected: 1)" << endl;
    
    // Test Case 3
    cout << "factorial(1) = " << factorial(1) << " (Expected: 1)" << endl;
    
    // Test Case 4
    cout << "factorial(3) = " << factorial(3) << " (Expected: 6)" << endl;
    
    // Test Case 5
    cout << "factorial(10) = " << factorial(10) << " (Expected: 3628800)" << endl;
    
    return 0;
}
