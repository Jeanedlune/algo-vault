package reverseinteger

// ReverseInteger reverses digits of a 32-bit signed integer. Returns 0 on overflow.
// Time: O(k), Space: O(1)
func ReverseInteger(x int) int {
    const INT_MIN = -2147483648
    const INT_MAX = 2147483647

    a := int64(x)
    sign := int64(1)
    if a < 0 {
        sign = -1
        a = -a
    }

    var rev int64 = 0
    for a != 0 {
        digit := a % 10
        a /= 10
        if rev > (int64(INT_MAX)-digit)/10 {
            return 0
        }
        rev = rev*10 + digit
    }
    rev *= sign
    if rev < int64(INT_MIN) || rev > int64(INT_MAX) {
        return 0
    }
    return int(rev)
}
