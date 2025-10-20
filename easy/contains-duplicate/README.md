# Contains Duplicate

**Difficulty:** Easy  

## Problem
Given an integer array `nums`, determine whether any value appears at least twice in the array.  
Return `true` if any element is repeated, otherwise `false`.

### Example 1
Input: `[1, 2, 3, 1]`  
Output: `true`

### Example 2
Input: `[1, 2, 3, 4]`  
Output: `false`

### Example 3
Input: `[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`  
Output: `true`

## Constraints
- `1 ≤ nums.length ≤ 10⁵`
- `-10⁹ ≤ nums[i] ≤ 10⁹`

## Test Cases
| Input | Expected Output |
|:------|:----------------|
| [1,2,3,1] | true |
| [1,2,3,4] | false |
| [1,1,1,3,3,4,3,2,4,2] | true |
| [] | false |
| [42] | false |

## Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)
