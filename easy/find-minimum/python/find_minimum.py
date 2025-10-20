from typing import List


def find_minimum(arr: List[int]) -> int:
    """
    Returns the smallest element in the array.

    Args:
        arr (List[int]): List of integers

    Returns:
        int: Minimum value in the array

    Raises:
        ValueError: If the input list is empty
    """
    if not arr:
        raise ValueError("Input array is empty")
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum


# Simple test harness
if __name__ == "__main__":
    test_cases = [
        ([3, 1, 4, 1, 5], 1),
        ([10, 20, 5, 30, 2], 2),
        ([7], 7),
        ([5, 5, 5], 5),
        ([-10, 0, 5, -3], -10),
    ]

    for arr, expected in test_cases:
        result = find_minimum(arr)
        assert (
            result == expected
        ), f"Failed for {arr}: expected {expected}, got {result}"
    print("All test cases passed.")
