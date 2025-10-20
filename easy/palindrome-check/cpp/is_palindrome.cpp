#include <string>
#include <algorithm>
#include <cctype>

class Solution {
public:
    bool isPalindrome(std::string s) {
        std::string sanitized = "";
        for (char c : s) {
            if (std::isalnum(c)) {
                sanitized += std::tolower(c);
            }
        }

        std::string reversed = sanitized;
        std::reverse(reversed.begin(), reversed.end());

        return sanitized == reversed;
    }
};
