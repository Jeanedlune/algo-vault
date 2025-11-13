# Sum of Array

Given an array of integers, return the sum of all elements in the array.

## Examples

### Example 1
```
Input: [1, 2, 3, 4, 5]
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15
```

### Example 2
```
Input: [-1, -2, -3, -4, -5]
Output: -15
Explanation: -1 + -2 + -3 + -4 + -5 = -15
```

### Example 3
```
Input: [0, 0, 0, 0]
Output: 0
Explanation: 0 + 0 + 0 + 0 = 0
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- The sum will fit within a 64-bit signed integer

## Test Cases

1. `[1, 2, 3, 4, 5]` → `15`
2. `[-1, -2, -3, -4, -5]` → `-15`
3. `[0, 0, 0, 0]` → `0`
4. `[1000000000]` → `1000000000`
5. `[1, -1, 2, -2, 3, -3]` → `0`

## Target Complexity

- **Time:** O(n) - where n is the length of the array
- **Space:** O(1) - constant extra space
