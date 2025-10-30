#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int countVowels(const string& s) {
    int count = 0;
    for (char c : s) {
        char lower = tolower(c);
        if (lower == 'a' || lower == 'e' || lower == 'i' || 
            lower == 'o' || lower == 'u') {
            count++;
        }
    }
    return count;
}

int main() {
    // Test Case 1
    cout << "countVowels(\"hello world\") = " << countVowels("hello world") 
         << " (Expected: 3)" << endl;
    
    // Test Case 2
    cout << "countVowels(\"AEIOU\") = " << countVowels("AEIOU") 
         << " (Expected: 5)" << endl;
    
    // Test Case 3
    cout << "countVowels(\"xyz\") = " << countVowels("xyz") 
         << " (Expected: 0)" << endl;
    
    // Test Case 4
    cout << "countVowels(\"\") = " << countVowels("") 
         << " (Expected: 0)" << endl;
    
    // Test Case 5
    cout << "countVowels(\"ChatGPT rocks!\") = " << countVowels("ChatGPT rocks!") 
         << " (Expected: 2)" << endl;
    
    return 0;
}
