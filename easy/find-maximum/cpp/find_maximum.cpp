#include <vector>
#include <stdexcept>
using namespace std;

int findMaximum(const vector<int>& nums) {
    if (nums.empty()) {
        throw invalid_argument("Array must not be empty");
    }
    
    int max = nums[0];
    for (int i = 1; i < (int)nums.size(); ++i) {
        if (nums[i] > max) {
            max = nums[i];
        }
    }
    return max;
}