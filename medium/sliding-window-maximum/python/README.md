# Sliding Window Maximum

## Problem
Given an array `nums` and an integer `k`, find the maximum value in each sliding window of size `k`.

## Constraints
1 <= nums.length <= 10^5  
-10^4 <= nums[i] <= 10^4  
1 <= k <= nums.length

## Examples

### Example 1
Input: [1,3,-1,-3,5,3,6,7], k=3  
Output: [3, 3, 5, 5, 6, 7]

### Example 2
Input: [1], k=1  
Output: [1]

### Example 3
Input: [], k=1  
Output: []

### Example 4
Input: [4,2,12,3], k=4  
Output: [12]

### Example 5
Input: [4,2,12,3], k=1  
Output: [4, 2, 12, 3]

## Solution
- Time Complexity: O(n)  
- Space Complexity: O(k)  
- Uses a deque to maintain the maximum efficiently.

## Test Cases
```python
assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert sliding_window_max([1], 1) == [1]
assert sliding_window_max([], 1) == []
assert sliding_window_max([4, 2, 12, 3], 4) == [12]
assert sliding_window_max([4, 2, 12, 3], 1) == [4, 2, 12, 3]
