from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    """
    Move all zeros in the list to the end while maintaining
    the relative order of non-zero elements.

    Args:
        nums (List[int]): The input list of integers.

    Returns:
        List[int]: The list after moving all zeros to the end.
    """
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
    return nums


if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([4, 0, 5, 0, 0, 3, 2], [4, 5, 3, 2, 0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
    ]

    for arr, expected in test_cases:
        result = move_zeroes(arr.copy())
        assert (
            result == expected
        ), f"Failed for {arr}: expected {expected}, got {result}"
    print("All test cases passed.")
