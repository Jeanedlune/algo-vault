from typing import List


def find_maximum(nums: List[int]) -> int:
    if not nums:
        raise ValueError("Array must not be empty")

    max_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
    return max_val
