def reverse_integer(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    while x:
        digit = x % 10
        x //= 10
        # Check overflow before multiplying by 10 and adding digit
        if rev > (INT_MAX - digit) // 10:
            return 0
        rev = rev * 10 + digit
    rev *= sign
    if rev < INT_MIN or rev > INT_MAX:
        return 0
    return rev

