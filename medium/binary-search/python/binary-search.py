# medium/binary-search/python/binary-search.py
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Binary Search Algorithm

    Given a sorted list of integers `nums` and a target value `target`,
    return the index of `target` if found; otherwise return -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Verification block for simple testing
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 7, 9], 7, 3),
        ([1, 2, 3, 4, 5], 6, -1),
        ([-5, -1, 0, 3, 9, 12], -1, 1),
        ([1], 1, 0),
        ([1, 1, 1, 1], 1, "any 0..3"),
    ]

    for nums, target, expected in test_cases:
        result = binary_search(nums, target)
        print(f"nums={nums}, target={target} → result={result}, expected={expected}")
