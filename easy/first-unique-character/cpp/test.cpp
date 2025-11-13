#include <iostream>
#include <string>
#include <cassert>
#include "solution.cpp"

using namespace std;

int main() {
    Solution sol;
    
    // Test case 1
    string s1 = "leetcode";
    assert(sol.firstUniqueChar(s1) == 0);
    assert(sol.firstUniqueCharOptimized(s1) == 0);
    cout << "Test case 1 passed!" << endl;
    
    // Test case 2
    string s2 = "loveleetcode";
    assert(sol.firstUniqueChar(s2) == 2);
    assert(sol.firstUniqueCharOptimized(s2) == 2);
    cout << "Test case 2 passed!" << endl;
    
    // Test case 3
    string s3 = "aabb";
    assert(sol.firstUniqueChar(s3) == -1);
    assert(sol.firstUniqueCharOptimized(s3) == -1);
    cout << "Test case 3 passed!" << endl;
    
    // Test case 4
    string s4 = "z";
    assert(sol.firstUniqueChar(s4) == 0);
    assert(sol.firstUniqueCharOptimized(s4) == 0);
    cout << "Test case 4 passed!" << endl;
    
    // Test case 5
    string s5 = "aabbccddeeffg";
    assert(sol.firstUniqueChar(s5) == 12);
    assert(sol.firstUniqueCharOptimized(s5) == 12);
    cout << "Test case 5 passed!" << endl;
    
    cout << "All test cases passed!" << endl;
    return 0;
}
