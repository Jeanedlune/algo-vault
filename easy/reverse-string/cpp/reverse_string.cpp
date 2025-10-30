#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string reverseString(const string& s) {
    string result = s;
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    // Test Case 1
    cout << "Test 1: " << reverseString("hello") << " (Expected: olleh)" << endl;
    
    // Test Case 2
    cout << "Test 2: " << reverseString("Hacktoberfest") << " (Expected: tsefrebotkcaH)" << endl;
    
    // Test Case 3
    cout << "Test 3: " << reverseString("Python") << " (Expected: nohtyP)" << endl;
    
    // Test Case 4
    cout << "Test 4: " << reverseString("a") << " (Expected: a)" << endl;
    
    // Test Case 5
    cout << "Test 5: " << reverseString("") << " (Expected: )" << endl;
    
    return 0;
}
