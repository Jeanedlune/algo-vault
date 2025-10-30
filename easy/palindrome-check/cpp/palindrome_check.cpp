#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(const string& s) {
    int left = 0;
    int right = s.length() - 1;
    
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    // Test Case 1
    cout << "isPalindrome(\"racecar\") = " << (isPalindrome("racecar") ? "true" : "false") 
         << " (Expected: true)" << endl;
    
    // Test Case 2
    cout << "isPalindrome(\"hello\") = " << (isPalindrome("hello") ? "true" : "false") 
         << " (Expected: false)" << endl;
    
    // Test Case 3
    cout << "isPalindrome(\"madam\") = " << (isPalindrome("madam") ? "true" : "false") 
         << " (Expected: true)" << endl;
    
    // Test Case 4
    cout << "isPalindrome(\"level\") = " << (isPalindrome("level") ? "true" : "false") 
         << " (Expected: true)" << endl;
    
    // Test Case 5
    cout << "isPalindrome(\"\") = " << (isPalindrome("") ? "true" : "false") 
         << " (Expected: true)" << endl;
    
    return 0;
}
