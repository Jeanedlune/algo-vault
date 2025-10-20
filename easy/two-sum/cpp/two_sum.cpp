#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int,int> m;
    for (int i = 0; i < (int)nums.size(); ++i) {
        int want = target - nums[i];
        auto it = m.find(want);
        if (it != m.end()) return {it->second, i};
        m[nums[i]] = i;
    }
    return {};
}
