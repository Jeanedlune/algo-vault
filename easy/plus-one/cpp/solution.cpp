#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        
        // Start from the last digit
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            
            // If current digit is 9, it becomes 0 and we carry over
            digits[i] = 0;
        }
        
        // If we're here, all digits were 9, so we need to add a 1 at the beginning
        digits.insert(digits.begin(), 1);
        return digits;
    }
    
    // Alternative solution without using insert
    vector<int> plusOneAlternative(vector<int>& digits) {
        int n = digits.size();
        
        // Start from the last digit
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            
            digits[i] = 0;
        }
        
        // If we're here, all digits were 9, create a new array
        vector<int> result(n + 1, 0);
        result[0] = 1;
        return result;
    }
};
