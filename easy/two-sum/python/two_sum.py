from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, v in enumerate(nums):
        w = target - v
        if w in seen:
            return [seen[w], i]
        seen[v] = i
    return []
