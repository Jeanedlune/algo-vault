# Trapping Rain Water

Given a list of non-negative integers representing elevation heights, compute how much water can be trapped after raining.

## Examples

Input:
```
[0,1,0,2,1,0,1,3,2,1,2,1]
```
Output:
```
6
```

Input:
```
[4,2,0,3,2,5]
```
Output:
```
9
```

Input:
```
[2,0,2]
```
Output:
```
2
```

## Constraints
- 1 <= height.length <= 2 * 10^4
- 0 <= height[i] <= 10^5

## Test cases (3–5)
- [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
- [4,2,0,3,2,5] -> 9
- [2,0,2] -> 2
- [1,0,0,0,1] -> 3
- [3,0,0,2,0,4] -> 10

## Target complexity
- Time: O(n)
- Space: O(1)
