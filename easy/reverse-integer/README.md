# Reverse Integer

Reverse the digits of a 32-bit signed integer. If reversing the integer causes it to go outside the 32-bit signed integer range, return 0.

Let x be an integer. Return the reversed integer.

Note: Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Examples

Input:
```
x = 123
```
Output:
```
321
```

Input:
```
x = -123
```
Output:
```
-321
```

Input:
```
x = 120
```
Output:
```
21
```

Input:
```
x = 1534236469
```
Output:
```
0  // overflow when reversed
```

## Constraints
- -2^31 <= x <= 2^31 - 1 (i.e., [-2147483648, 2147483647])
- Reversal must detect overflow and return 0 on overflow

## Test cases (3–5)
- x = 123 -> 321
- x = -123 -> -321
- x = 120 -> 21
- x = 0 -> 0
- x = 1534236469 -> 0 (overflow)

## Target complexity
- Time: O(k), where k is the number of digits in x
- Space: O(1)

---

This problem is part of the Hacktoberfest algo-vault project. Please follow the repository's guidelines in `CONTRIBUTING.md` for structure, code style, and PRs.
