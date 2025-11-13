#include <iostream>
#include <vector>
#include <cassert>
#include "solution.cpp"

using namespace std;

void printVector(const vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); ++i) {
        cout << v[i];
        if (i < (int)v.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    Solution sol;
    
    // Test case 1
    vector<int> digits1 = {1,2,3};
    vector<int> result1 = {1,2,4};
    assert(sol.plusOne(digits1) == result1);
    
    vector<int> digits1_alt = {1,2,3};
    assert(sol.plusOneAlternative(digits1_alt) == result1);
    cout << "Test case 1 passed!" << endl;
    
    // Test case 2
    vector<int> digits2 = {4,3,2,1};
    vector<int> result2 = {4,3,2,2};
    assert(sol.plusOne(digits2) == result2);
    
    vector<int> digits2_alt = {4,3,2,1};
    assert(sol.plusOneAlternative(digits2_alt) == result2);
    cout << "Test case 2 passed!" << endl;
    
    // Test case 3
    vector<int> digits3 = {9};
    vector<int> result3 = {1,0};
    assert(sol.plusOne(digits3) == result3);
    
    vector<int> digits3_alt = {9};
    assert(sol.plusOneAlternative(digits3_alt) == result3);
    cout << "Test case 3 passed!" << endl;
    
    // Test case 4
    vector<int> digits4 = {9,9,9};
    vector<int> result4 = {1,0,0,0};
    assert(sol.plusOne(digits4) == result4);
    
    vector<int> digits4_alt = {9,9,9};
    assert(sol.plusOneAlternative(digits4_alt) == result4);
    cout << "Test case 4 passed!" << endl;
    
    // Test case 5
    vector<int> digits5 = {0};
    vector<int> result5 = {1};
    assert(sol.plusOne(digits5) == result5);
    
    vector<int> digits5_alt = {0};
    assert(sol.plusOneAlternative(digits5_alt) == result5);
    cout << "Test case 5 passed!" << endl;
    
    cout << "All test cases passed!" << endl;
    return 0;
}
