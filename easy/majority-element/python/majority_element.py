from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Finds the majority element in a list of numbers.

    The majority element is the element that appears more than ⌊n / 2⌋ times.

    This implementation uses the Boyer-Moore Voting Algorithm.

    Args:
        nums: A list of integers.

    Returns:
        The majority element.
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate
