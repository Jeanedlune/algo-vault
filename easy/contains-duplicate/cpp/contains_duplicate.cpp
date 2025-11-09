#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool containsDuplicate(const vector<int>& nums) {
    unordered_set<int> seen;
    
    for (int num : nums) {
        if (seen.count(num) > 0) {
            return true;
        }
        seen.insert(num);
    }
    
    return false;
}

int main() {
    // Test cases
    cout << boolalpha;
    cout << containsDuplicate({1, 2, 3, 1}) << endl; // true
    cout << containsDuplicate({1, 2, 3, 4}) << endl; // false
    cout << containsDuplicate({1, 1, 1, 3, 3, 4, 3, 2, 4, 2}) << endl; // true
    cout << containsDuplicate({}) << endl; // false
    cout << containsDuplicate({42}) << endl; // false
    
    return 0;
}
