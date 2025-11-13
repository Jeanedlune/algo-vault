#include <iostream>
#include <vector>
#include <cassert>
#include "solution.cpp"

using namespace std;

int main() {
    Solution sol;
    
    // Test case 1
    vector<int> nums1 = {2,2,1};
    assert(sol.singleNumberXOR(nums1) == 1);
    assert(sol.singleNumberHash(nums1) == 1);
    cout << "Test case 1 passed!" << endl;
    
    // Test case 2
    vector<int> nums2 = {4,1,2,1,2};
    assert(sol.singleNumberXOR(nums2) == 4);
    assert(sol.singleNumberHash(nums2) == 4);
    cout << "Test case 2 passed!" << endl;
    
    // Test case 3
    vector<int> nums3 = {1};
    assert(sol.singleNumberXOR(nums3) == 1);
    assert(sol.singleNumberHash(nums3) == 1);
    cout << "Test case 3 passed!" << endl;
    
    // Test case 4
    vector<int> nums4 = {-1,0,0};
    assert(sol.singleNumberXOR(nums4) == -1);
    assert(sol.singleNumberHash(nums4) == -1);
    cout << "Test case 4 passed!" << endl;
    
    // Test case 5
    vector<int> nums5 = {2,2,3,3,4,4,5};
    assert(sol.singleNumberXOR(nums5) == 5);
    assert(sol.singleNumberHash(nums5) == 5);
    cout << "Test case 5 passed!" << endl;
    
    cout << "All test cases passed!" << endl;
    return 0;
}
