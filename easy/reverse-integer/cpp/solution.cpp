#include <climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long reversed = 0;
        
        while (x != 0) {
            int digit = x % 10;
            x /= 10;
            
            reversed = reversed * 10 + digit;
            
            // Check for overflow
            if (reversed > INT_MAX || reversed < INT_MIN) {
                return 0;
            }
        }
        
        return (int)reversed;
    }
    
    // Alternative solution without using long long
    int reverseSafe(int x) {
        int reversed = 0;
        
        while (x != 0) {
            int digit = x % 10;
            x /= 10;
            
            // Check for overflow before multiplying
            if (reversed > INT_MAX / 10 || reversed < INT_MIN / 10) {
                return 0;
            }
            
            reversed = reversed * 10 + digit;
        }
        
        return reversed;
    }
};
