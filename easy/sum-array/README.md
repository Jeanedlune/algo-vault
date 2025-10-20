# Sum of Array

Given an array of integers `nums`, return the sum of all elements.

## Examples

Input:
```
nums = [1, 2, 3, 4, 5]
```
Output:
```
15
```

Input:
```
nums = [-2, 0, 2]
```
Output:
```
0
```

## Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- Use 32-bit integer accumulation where applicable; if language integers are unbounded (e.g., Python), standard int is fine.

## Test cases (3–5)
- nums = [1,2,3,4,5] -> 15
- nums = [] -> 0
- nums = [-2, 0, 2] -> 0
- nums = [100000, 200000, 300000] -> 600000
- nums = [-1, -1, -1, -1] -> -4

## Target complexity
- Time: O(n)
- Space: O(1)

---

This problem is part of the Hacktoberfest algo-vault project. Please follow the repository's guidelines in `CONTRIBUTING.md` for structure, code style, and PRs.