from collections import deque
from typing import List

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    """
    Finds the maximum value in each sliding window of size k.

    Args:
        nums (List[int]): List of integers.
        k (int): Size of the sliding window.

    Returns:
        List[int]: List of maximums for each sliding window.
    """
    if not nums or k <= 0:
        return []

    result: List[int] = []
    window_indices: deque[int] = deque()  # stores indices of elements in current window

    for i in range(len(nums)):
        # remove indices out of current window
        while window_indices and window_indices[0] < i - k + 1:
            window_indices.popleft()

        # remove smaller numbers at the end
        while window_indices and nums[window_indices[-1]] < nums[i]:
            window_indices.pop()

        window_indices.append(i)

        # add max to result (front of deque)
        if i >= k - 1:
            result.append(nums[window_indices[0]])

    return result


# Example test harness
if __name__ == "__main__":
    # Test Case 1
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    # Test Case 2: Single element
    assert sliding_window_max([1], 1) == [1]
    # Test Case 3: Empty list
    assert sliding_window_max([], 1) == []
    # Test Case 4: Window size equals list length
    assert sliding_window_max([4, 2, 12, 3], 4) == [12]
    # Test Case 5: Window size 1
    assert sliding_window_max([4, 2, 12, 3], 1) == [4, 2, 12, 3]

    print("All tests passed!")
