#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    long long sumArray(const vector<int>& nums) {
        long long sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;
    }
    
    // Alternative solution using std::accumulate
    long long sumArrayAlternative(const vector<int>& nums) {
        return accumulate(nums.begin(), nums.end(), 0LL);
    }
};
