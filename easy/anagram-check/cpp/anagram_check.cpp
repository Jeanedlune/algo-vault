#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length()) {
        return false;
    }
    
    unordered_map<char, int> charCount;
    
    // Count characters in s
    for (char c : s) {
        charCount[c]++;
    }
    
    // Decrement count for characters in t
    for (char c : t) {
        charCount[c]--;
        if (charCount[c] < 0) {
            return false;
        }
    }
    
    return true;
}

int main() {
    // Test cases
    cout << boolalpha;
    cout << isAnagram("anagram", "nagaram") << endl; // true
    cout << isAnagram("rat", "car") << endl; // false
    cout << isAnagram("listen", "silent") << endl; // true
    cout << isAnagram("hello", "world") << endl; // false
    cout << isAnagram("aacc", "ccac") << endl; // false
    cout << isAnagram("railsafety", "fairytales") << endl; // true
    cout << isAnagram("dormitory", "dirtyroom") << endl; // true
    
    return 0;
}
