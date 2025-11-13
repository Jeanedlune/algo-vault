# Plus One

Given a non-empty array of decimal digits representing a non-negative integer, increment the integer by one and return the resulting array of digits.

## Examples

### Example 1
```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123, and 123 + 1 = 124.
```

### Example 2
```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321, and 4321 + 1 = 4322.
```

### Example 3
```
Input: [9]
Output: [1,0]
Explanation: The array represents the integer 9, and 9 + 1 = 10.
```

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading zeros

## Test Cases

1. `[1,2,3]` → `[1,2,4]`
2. `[4,3,2,1]` → `[4,3,2,2]`
3. `[9]` → `[1,0]`
4. `[9,9,9]` → `[1,0,0,0]`
5. `[0]` → `[1]`

## Target Complexity

- **Time:** O(n) - where n is the length of the digits array
- **Space:** O(1) - constant extra space (excluding output)
