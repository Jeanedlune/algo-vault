#include <iostream>
#include <vector>
using namespace std;

vector<int> fibonacci(int n) {
    if (n == 0) {
        return {};
    }
    
    vector<int> result;
    
    if (n >= 1) {
        result.push_back(0);
    }
    if (n >= 2) {
        result.push_back(1);
    }
    
    for (int i = 2; i < n; ++i) {
        result.push_back(result[i - 1] + result[i - 2]);
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
    printVector(fibonacci(0)); // []
    printVector(fibonacci(1)); // [0]
    printVector(fibonacci(2)); // [0,1]
    printVector(fibonacci(5)); // [0,1,1,2,3]
    printVector(fibonacci(7)); // [0,1,1,2,3,5,8]
    
    return 0;
}
