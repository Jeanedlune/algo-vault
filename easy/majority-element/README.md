# Majority Element

Find the element that appears more than ⌊n / 2⌋ times in an array of size n.

## Input/Output Examples

### Example 1:

- **Input**: `[3, 2, 3]`
- **Output**: `3`

### Example 2:

- **Input**: `[2, 2, 1, 1, 1, 2, 2]`
- **Output**: `2`

### Example 3:

- **Input**: `[1]`
- **Output**: `1`

## Constraints

- The array is non-empty.
- The majority element always exists in the array.
- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Test Cases

1. `[3, 2, 3]` -> `3`
2. `[2, 2, 1, 1, 1, 2, 2]` -> `2`
3. `[1]` -> `1`
4. `[6, 5, 5]` -> `5`
5. `[1, 2, 3, 4, 5, 5, 5, 5, 5]` -> `5`

## Target Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
