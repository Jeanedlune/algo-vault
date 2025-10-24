from typing import List


def remove_duplicates(nums: List[int]) -> List[int]:
    """Remove duplicates from a sorted array."""
    if not nums:
        return []

    unique = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            unique.append(nums[i])
    return unique


if __name__ == "__main__":
    tests = [
        [1, 1, 2, 2, 3],
        [0, 0, 0, 0],
        [1, 2, 3, 4],
        [],
        [5, 5, 6, 7, 7, 7, 8],
    ]
    for t in tests:
        print(f"{t} → {remove_duplicates(t)}")
