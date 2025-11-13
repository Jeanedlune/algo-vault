# Single Number

Given a non-empty array of integers where every element appears twice except for one, find the element that appears only once.

## Examples

### Example 1
```
Input: [2,2,1]
Output: 1
```

### Example 2
```
Input: [4,1,2,1,2]
Output: 4
```

### Example 3
```
Input: [1]
Output: 1
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element appears exactly twice except for one element which appears once.

## Test Cases

1. `[2,2,1]` → `1`
2. `[4,1,2,1,2]` → `4`
3. `[1]` → `1`
4. `[-1,0,0]` → `-1`
5. `[2,2,3,3,4,4,5]` → `5`

## Target Complexity

- **Time:** O(n) - where n is the length of the array
- **Space:** O(1) - constant extra space
