from typing import List

def single_number(nums: List[int]) -> int:
    """
    Finds the single element in a list where every other element appears twice.

    This implementation uses the XOR bitwise operator. The XOR of a number with
    itself is 0. So, XORing all elements will cancel out the pairs, leaving
    the unique number.

    Args:
        nums: A list of integers where every element appears twice except for one.

    Returns:
        The single, non-duplicate number.
    """
    result = 0
    for num in nums:
        result ^= num
    return result
