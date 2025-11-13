#include <iostream>
#include <vector>
#include <cassert>
#include "solution.cpp"

using namespace std;

int main() {
    Solution sol;
    
    // Test case 1
    vector<int> nums1 = {1, 2, 3, 4, 5};
    assert(sol.sumArray(nums1) == 15);
    assert(sol.sumArrayAlternative(nums1) == 15);
    cout << "Test case 1 passed!" << endl;
    
    // Test case 2
    vector<int> nums2 = {-1, -2, -3, -4, -5};
    assert(sol.sumArray(nums2) == -15);
    assert(sol.sumArrayAlternative(nums2) == -15);
    cout << "Test case 2 passed!" << endl;
    
    // Test case 3
    vector<int> nums3 = {0, 0, 0, 0};
    assert(sol.sumArray(nums3) == 0);
    assert(sol.sumArrayAlternative(nums3) == 0);
    cout << "Test case 3 passed!" << endl;
    
    // Test case 4
    vector<int> nums4 = {1000000000};
    assert(sol.sumArray(nums4) == 1000000000);
    assert(sol.sumArrayAlternative(nums4) == 1000000000);
    cout << "Test case 4 passed!" << endl;
    
    // Test case 5
    vector<int> nums5 = {1, -1, 2, -2, 3, -3};
    assert(sol.sumArray(nums5) == 0);
    assert(sol.sumArrayAlternative(nums5) == 0);
    cout << "Test case 5 passed!" << endl;
    
    cout << "All test cases passed!" << endl;
    return 0;
}
