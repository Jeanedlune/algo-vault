from typing import List


def fibonacci(n: int) -> List[int]:
    """
    Generate the Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms in the sequence.

    Returns:
        List[int]: List containing the Fibonacci sequence up to n terms.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    test_cases = [
        (7, [0, 1, 1, 2, 3, 5, 8]),
        (1, [0]),
        (2, [0, 1]),
        (0, []),
        (5, [0, 1, 1, 2, 3]),
    ]

    for n, expected in test_cases:
        result = fibonacci(n)
        assert (
            result == expected
        ), f"Failed for n={n}: expected {expected}, got {result}"
    print("All test cases passed.")
