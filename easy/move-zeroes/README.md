# Move Zeroes

## Problem Description
Given an integer array, move all zeros to the end while maintaining the relative order of non-zero elements.

### Example
**Input:** `[0, 1, 0, 3, 12]`  
**Output:** `[1, 3, 12, 0, 0]`

### Constraints
- Modify the array in-place.
- Maintain the order of non-zero elements.
- Handle arrays with all zeros or no zeros gracefully.

### Test Cases
| Input | Expected Output |
|--------|-----------------|
| [0, 1, 0, 3, 12] | [1, 3, 12, 0, 0] |
| [0, 0, 1] | [1, 0, 0] |
| [4, 0, 5, 0, 0, 3, 2] | [4, 5, 3, 2, 0, 0, 0] |
| [1, 2, 3] | [1, 2, 3] |
| [0, 0, 0] | [0, 0, 0] |

### Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Languages
Implementations available or planned for:
- ✅ Python  
- ⬜ C++  
- ⬜ C#  
- ⬜ Go  
- ⬜ TypeScript  
- ⬜ JavaScript
