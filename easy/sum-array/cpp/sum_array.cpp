#include <vector>

// Sum of Array - C++17
// Time: O(n), Space: O(1)

int sumArray(const std::vector<int>& nums) {
    int total = 0;
    for (int v : nums) total += v;
    return total;
}
