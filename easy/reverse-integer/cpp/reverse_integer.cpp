#include <limits>

// Reverse Integer - C++17 (32-bit arithmetic only)
// Time: O(k), Space: O(1)

int reverseInteger(int x) {
    const int INT_MIN = std::numeric_limits<int>::min();
    const int INT_MAX = std::numeric_limits<int>::max();

    int rev = 0;
    while (x != 0) {
        int pop = x % 10;
        x /= 10;
        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
        rev = rev * 10 + pop;
    }
    return rev;
}
