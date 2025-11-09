#include <iostream>
#include <vector>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int nonZeroPos = 0;
    
    // Move all non-zero elements to the front
    for (int i = 0; i < (int)nums.size(); ++i) {
        if (nums[i] != 0) {
            nums[nonZeroPos] = nums[i];
            ++nonZeroPos;
        }
    }
    
    // Fill remaining positions with zeros
    for (int i = nonZeroPos; i < (int)nums.size(); ++i) {
        nums[i] = 0;
    }
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
    vector<int> test1 = {0, 1, 0, 3, 12};
    moveZeroes(test1);
    printVector(test1); // [1,3,12,0,0]
    
    vector<int> test2 = {0, 0, 1};
    moveZeroes(test2);
    printVector(test2); // [1,0,0]
    
    vector<int> test3 = {4, 5, 6};
    moveZeroes(test3);
    printVector(test3); // [4,5,6]
    
    vector<int> test4 = {0, 0, 0};
    moveZeroes(test4);
    printVector(test4); // [0,0,0]
    
    vector<int> test5 = {1, 0, 2, 0, 3, 0};
    moveZeroes(test5);
    printVector(test5); // [1,2,3,0,0,0]
    
    return 0;
}
