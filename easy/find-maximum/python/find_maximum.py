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


if __name__ == "__main__":
    tests = [
        ([1, 5, 3, 9, 2], 9),
        ([42], 42),
        ([-5, -1, -8, -3], -1),
        ([100, 50, 25, 10], 100),
        ([7, 9, 3, 9, 1], 9),
    ]

    for nums, expected in tests:
        result = find_maximum(nums)
        if result == expected:
            print(f"✅ Test passed: {nums} → {result}")
        else:
            print(f"❌ Test failed: {nums} → expected {expected}, got {result}")
