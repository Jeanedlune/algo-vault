#include <limits>

// Reverse Integer - C++17
// Time: O(k), Space: O(1)

int reverseInteger(int x) {
    const int INT_MIN = std::numeric_limits<int>::min();
    const int INT_MAX = std::numeric_limits<int>::max();

    long long a = x; // use 64-bit to safely take abs and accumulate
    int sign = 1;
    if (a < 0) { sign = -1; a = -a; }

    long long rev = 0;
    while (a != 0) {
        int digit = static_cast<int>(a % 10);
        a /= 10;
        if (rev > (static_cast<long long>(INT_MAX) - digit) / 10) return 0;
        rev = rev * 10 + digit;
    }
    rev *= sign;
    if (rev < INT_MIN || rev > INT_MAX) return 0;
    return static_cast<int>(rev);
}
