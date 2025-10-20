from typing import List


def remove_duplicates(nums: List[int]) -> List[int]:
    """
    Remove duplicates from a sorted list and return the new list
    with unique elements, maintaining order.

    Args:
        nums (List[int]): Sorted list of integers (may contain duplicates).

    Returns:
        List[int]: List of unique elements.
    """
    if not nums:
        return []

    unique = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            unique.append(nums[i])
    return unique


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2, 2, 3], [1, 2, 3]),
        ([0, 0, 1, 1, 1, 2, 2, 3], [0, 1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([5, 5, 5, 5], [5]),
        ([], []),
    ]

    for arr, expected in test_cases:
        result = remove_duplicates(arr)
        assert (
            result == expected
        ), f"Failed for {arr}: expected {expected}, got {result}"
    print("All test cases passed.")
