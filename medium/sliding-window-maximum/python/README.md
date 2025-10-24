# Sliding Window Maximum

## Problem
Given an array `nums` and an integer `k`, find the maximum value in each sliding window of size `k`.

### Example
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [3,3,-1,3,5,6,7]

## Solution
- Time Complexity: O(n)
- Space Complexity: O(k)
- Uses a deque to maintain the maximum efficiently.

## Test cases
```python
assert sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3,3,-1,3,5,6,7]
assert sliding_window_max([1], 1) == [1]
assert sliding_window_max([], 1) == []
