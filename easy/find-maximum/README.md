# Find Maximum in Array

## Problem Statement

Given an array of integers, find and return the maximum element in the array.

## Examples

### Example 1

**Input:** `[1, 5, 3, 9, 2]`  
**Output:** `9`  
**Explanation:** 9 is the largest element in the array.

### Example 2

**Input:** `[42]`  
**Output:** `42`  
**Explanation:** Single element is the maximum.

### Example 3

**Input:** `[-5, -1, -8, -3]`  
**Output:** `-1`  
**Explanation:** -1 is the largest among negative numbers.

## Constraints

- `1 <= array.length <= 10^5`
- `-10^9 <= array[i] <= 10^9`
- Array contains at least one element

## Test Cases

1. **Standard case:**
   - Input: `[1, 5, 3, 9, 2]`
   - Output: `9`

2. **Single element:**
   - Input: `[42]`
   - Output: `42`

3. **All negative numbers:**
   - Input: `[-5, -1, -8, -3]`
   - Output: `-1`

4. **Maximum at beginning:**
   - Input: `[100, 50, 25, 10]`
   - Output: `100`

5. **Duplicate maximums:**
   - Input: `[7, 9, 3, 9, 1]`
   - Output: `9`

## Complexity Analysis

- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only storing the maximum value

## Approach

1. Initialize the maximum value with the first element
2. Iterate through the array starting from the second element
3. Update the maximum if a larger element is found
4. Return the maximum value after the loop completes
