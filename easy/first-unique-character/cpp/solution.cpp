#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int firstUniqueChar(const string& s) {
        // Count frequency of each character
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        
        // Find first character with frequency 1
        for (int i = 0; i < (int)s.length(); ++i) {
            if (freq[s[i]] == 1) {
                return i;
            }
        }
        
        return -1;
    }
    
    // Alternative solution using array (more efficient for lowercase letters)
    int firstUniqueCharOptimized(const string& s) {
        vector<int> freq(26, 0);
        
        // Count frequency of each character
        for (char c : s) {
            freq[c - 'a']++;
        }
        
        // Find first character with frequency 1
        for (int i = 0; i < (int)s.length(); ++i) {
            if (freq[s[i] - 'a'] == 1) {
                return i;
            }
        }
        
        return -1;
    }
};
