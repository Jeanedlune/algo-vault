# Binary Search

Given a sorted array of integers `nums` and an integer `target`, return the index of `target` if it exists; otherwise return `-1`.

## Examples

Input:

```
nums = [1,3,5,7,9], target = 7
```

Output:

```
3
```

Input:

```
nums = [1,2,3,4,5], target = 6
```

Output:

```
-1
```

Input:

```
nums = [-5,-1,0,3,9,12], target = -1
```

Output:

```
1
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i], target <= 10^9
- `nums` is sorted in non-decreasing order
- Duplicates may exist; return any valid index if multiple matches

## Test cases (3–5)

- nums=[1,3,5,7,9], target=7 -> 3
- nums=[1,2,3,4,5], target=6 -> -1
- nums=[-5,-1,0,3,9,12], target=-1 -> 1
- nums=[1], target=1 -> 0
- nums=[1,1,1,1], target=1 -> any index 0..3

## Target complexity

- Time: O(log n)
- Space: O(1)
