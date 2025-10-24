from typing import List


def find_maximum(nums: List[int]) -> int:
    """
    Find the maximum element in an array.

    Args:
        nums: List of integers

    Returns:
        The maximum integer in the list

    Raises:
        ValueError: If the array is empty
    """
    if not nums:
        raise ValueError("Array must not be empty")

    max_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
    return max_val
