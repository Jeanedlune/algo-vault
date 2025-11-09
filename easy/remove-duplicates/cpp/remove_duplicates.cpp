#include <iostream>
#include <vector>
using namespace std;

vector<int> removeDuplicates(const vector<int>& nums) {
    if (nums.empty()) {
        return {};
    }
    
    vector<int> result;
    result.push_back(nums[0]);
    
    for (int i = 1; i < (int)nums.size(); ++i) {
        if (nums[i] != nums[i - 1]) {
            result.push_back(nums[i]);
        }
    }
    
    return result;
}

void printVector(const vector<int>& nums) {
    cout << "[";
    for (int i = 0; i < (int)nums.size(); ++i) {
        cout << nums[i];
        if (i < (int)nums.size() - 1) cout << ",";
    }
    cout << "]" << endl;
}

int main() {
    // Test cases
    printVector(removeDuplicates({1, 1, 2, 2, 3})); // [1,2,3]
    printVector(removeDuplicates({0, 0, 0, 0})); // [0]
    printVector(removeDuplicates({1, 2, 3, 4})); // [1,2,3,4]
    printVector(removeDuplicates({})); // []
    printVector(removeDuplicates({5, 5, 6, 7, 7, 7, 8})); // [5,6,7,8]
    
    return 0;
}
