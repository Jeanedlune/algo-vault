# Two Sum

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. Assume exactly one solution exists and you may not use the same element twice.

## Examples

Input:

```
nums = [2, 7, 11, 15], target = 9
```

Output:

```
[0, 1]
```

Input:

```
nums = [3, 2, 4], target = 6
```

Output:

```
[1, 2]
```

Input:

```
nums = [3, 3], target = 6
```

Output:

```
[0, 1]
```

## Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid answer exists

## Test cases (3–5)

- nums=[2,7,11,15], target=9 -> [0,1]
- nums=[3,2,4], target=6 -> [1,2]
- nums=[3,3], target=6 -> [0,1]
- nums=[-1,-2,-3,-4,-5], target=-8 -> [2,4]
- nums=[0,4,3,0], target=0 -> [0,3]

## Target complexity

- Time: O(n)
- Space: O(n)
