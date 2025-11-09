#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool isPalindrome(string s) {
    int left = 0;
    int right = s.length() - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters from left
        while (left < right && !isalnum(s[left])) {
            left++;
        }
        // Skip non-alphanumeric characters from right
        while (left < right && !isalnum(s[right])) {
            right--;
        }
        
        // Compare characters (case-insensitive)
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        
        left++;
        right--;
    }
    
    return true;
}

int main() {
    // Test cases
    cout << boolalpha;
    cout << isPalindrome("A man, a plan, a canal: Panama") << endl; // true
    cout << isPalindrome("race a car") << endl; // false
    cout << isPalindrome("Was it a car or a cat I saw?") << endl; // true
    cout << isPalindrome("tab a cat") << endl; // false
    cout << isPalindrome("") << endl; // true
    cout << isPalindrome(".,") << endl; // true
    cout << isPalindrome("ab@a") << endl; // true
    
    return 0;
}
