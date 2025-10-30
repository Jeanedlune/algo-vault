#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> fizzBuzz(int n) {
    vector<string> result;
    
    for (int i = 1; i <= n; ++i) {
        if (i % 15 == 0) {
            result.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            result.push_back("Fizz");
        } else if (i % 5 == 0) {
            result.push_back("Buzz");
        } else {
            result.push_back(to_string(i));
        }
    }
    
    return result;
}

void printVector(const vector<string>& v) {
    cout << "[";
    for (size_t i = 0; i < v.size(); ++i) {
        cout << "\"" << v[i] << "\"";
        if (i < v.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    // Test Case 1
    cout << "fizzBuzz(3) = ";
    printVector(fizzBuzz(3));
    cout << "Expected: [\"1\", \"2\", \"Fizz\"]" << endl << endl;
    
    // Test Case 2
    cout << "fizzBuzz(5) = ";
    printVector(fizzBuzz(5));
    cout << "Expected: [\"1\", \"2\", \"Fizz\", \"4\", \"Buzz\"]" << endl << endl;
    
    // Test Case 3
    cout << "fizzBuzz(15) = ";
    printVector(fizzBuzz(15));
    cout << "Expected: [\"1\", \"2\", \"Fizz\", \"4\", \"Buzz\", \"Fizz\", \"7\", \"8\", \"Fizz\", \"Buzz\", \"11\", \"Fizz\", \"13\", \"14\", \"FizzBuzz\"]" << endl;
    
    return 0;
}
