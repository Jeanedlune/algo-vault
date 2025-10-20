def count_vowels(s: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels present in the string.
    """
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


if __name__ == "__main__":
    test_cases = [
        ("hello world", 3),
        ("HACKTOBERFEST", 4),
        ("rhythm", 0),
        ("AEIOUaeiou", 10),
        ("Python", 1),
    ]

    for text, expected in test_cases:
        result = count_vowels(text)
        assert (
            result == expected
        ), f"Failed for {text}: expected {expected}, got {result}"
    print("All test cases passed.")
