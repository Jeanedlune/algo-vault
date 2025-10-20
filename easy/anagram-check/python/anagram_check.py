def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if s1 and s2 are anagrams, False otherwise.
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True


if __name__ == "__main__":
    test_cases = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("Dormitory", "Dirty room", True),
        ("School master", "The classroom", True),
        ("Astronomer", "Moon starer", True),
        ("rat", "car", False),
    ]

    for s1, s2, expected in test_cases:
        result = is_anagram(s1, s2)
        assert (
            result == expected
        ), f"Failed for {s1}, {s2}: expected {expected}, got {result}"
    print("All test cases passed.")
