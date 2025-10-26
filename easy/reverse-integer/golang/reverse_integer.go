package reverseinteger

// ReverseInteger reverses digits of a 32-bit signed integer. Returns 0 on overflow.
// Time: O(k), Space: O(1)
func ReverseInteger(x int) int {
    const INT_MIN = -2147483648
    const INT_MAX = 2147483647

    rev := 0
    for x != 0 {
        pop := x % 10
        x /= 10
        if rev > INT_MAX/10 || (rev == INT_MAX/10 && pop > 7) {
            return 0
        }
        if rev < INT_MIN/10 || (rev == INT_MIN/10 && pop < -8) {
            return 0
        }
        rev = rev*10 + pop
    }
    return rev
}
