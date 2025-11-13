#include <iostream>
#include <cassert>
#include "solution.cpp"

using namespace std;

int main() {
    Solution sol;
    
    // Test case 1
    assert(sol.reverse(123) == 321);
    assert(sol.reverseSafe(123) == 321);
    cout << "Test case 1 passed!" << endl;
    
    // Test case 2
    assert(sol.reverse(-123) == -321);
    assert(sol.reverseSafe(-123) == -321);
    cout << "Test case 2 passed!" << endl;
    
    // Test case 3
    assert(sol.reverse(120) == 21);
    assert(sol.reverseSafe(120) == 21);
    cout << "Test case 3 passed!" << endl;
    
    // Test case 4
    assert(sol.reverse(0) == 0);
    assert(sol.reverseSafe(0) == 0);
    cout << "Test case 4 passed!" << endl;
    
    // Test case 5 (overflow)
    assert(sol.reverse(1534236469) == 0);
    assert(sol.reverseSafe(1534236469) == 0);
    cout << "Test case 5 passed!" << endl;
    
    cout << "All test cases passed!" << endl;
    return 0;
}
