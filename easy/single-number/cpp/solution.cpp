#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // Solution using XOR (optimal O(1) space)
    int singleNumberXOR(const vector<int>& nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
    
    // Solution using hashmap (O(n) space)
    int singleNumberHash(const vector<int>& nums) {
        unordered_map<int, int> count;
        
        for (int num : nums) {
            count[num]++;
        }
        
        for (const auto& pair : count) {
            if (pair.second == 1) {
                return pair.first;
            }
        }
        
        return -1; // Should never reach here based on constraints
    }
};
