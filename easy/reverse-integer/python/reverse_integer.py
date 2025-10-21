def reverse_integer(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    rev = 0
    while x != 0:
        pop = x % 10 if x > 0 else x % -10
        x = x // 10 if x > 0 else -((-x) // 10)
        # Check overflow before applying
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0
        if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and pop < -8):
            return 0
        rev = rev * 10 + pop
    return rev

