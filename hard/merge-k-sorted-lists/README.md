# Merge K Sorted Lists

Given an array of `k` singly-linked lists where each list is sorted in ascending order, merge all the lists into one sorted list and return it.

For examples and testing in this repository, you may represent lists as arrays and provide the merged output as an array.

## Examples

Input:

```
lists = [[1,4,5],[1,3,4],[2,6]]
```

Output:

```
[1,1,2,3,4,4,5,6]
```

Input:

```
lists = [[]]
```

Output:

```
[]
```

Input:

```
lists = [[],[1]]
```

Output:

```
[1]
```

## Constraints

- 0 <= k <= 10^3
- Total number of elements across all lists N <= 10^5
- Values are within 32-bit signed integer range

## Test cases (3–5)

- [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
- [[]] -> []
- [[],[1]] -> [1]
- [[0,2,2],[1,1,3]] -> [0,1,1,2,2,3]

## Target complexity

- Time: O(N log k) where N is total elements
- Space: O(k) using a min-heap
