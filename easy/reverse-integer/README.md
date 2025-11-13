# Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

## Examples

### Example 1
```
Input: 123
Output: 321
```

### Example 2
```
Input: -123
Output: -321
```

### Example 3
```
Input: 120
Output: 21
```

### Example 4
```
Input: 0
Output: 0
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`
- If reversing the integer causes it to go outside the 32-bit signed integer range, return 0.

## Test Cases

1. `123` → `321`
2. `-123` → `-321`
3. `120` → `21`
4. `0` → `0`
5. `1534236469` → `0` (overflow case)

## Target Complexity

- **Time:** O(log n) - where n is the value of the integer
- **Space:** O(1) - constant extra space
