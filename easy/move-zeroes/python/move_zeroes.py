from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    """
    Moves all zeros to the end while maintaining the order of non-zero elements.
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums


if __name__ == "__main__":
    tests = [
        [0, 1, 0, 3, 12],
        [0, 0, 1],
        [4, 5, 6],
        [0, 0, 0],
        [1, 0, 2, 0, 3, 0],
    ]

    for t in tests:
        print(f"Input: {t} → Output: {move_zeroes(t[:])}")
