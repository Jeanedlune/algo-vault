#include <vector>
#include <numeric>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        return std::accumulate(nums.begin(), nums.end(), 0, std::bit_xor<int>());
    }
};
