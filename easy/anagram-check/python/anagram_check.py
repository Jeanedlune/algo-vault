# easy/anagram-check/python/anagram_check.py
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    Checks if two strings are anagrams of each other.

    Time Complexity: O(n), where n is the length of the strings.
    Space Complexity: O(k), where k is the number of unique characters.
    """
    # Anagrams must have the same length.
    if len(s) != len(t):
        return False

    # Count character frequencies and compare the counts.
    return Counter(s) == Counter(t)


# Verification block for simple testing
if __name__ == "__main__":
    # Test Case 1
    print(
        f"'listen' and 'silent' are anagrams: {is_anagram('listen', 'silent')}"
    )  # Expected: True

    # Test Case 2
    print(
        f"'hello' and 'world' are anagrams: {is_anagram('hello', 'world')}"
    )  # Expected: False

    # Test Case 3
    print(
        f"'aacc' and 'ccac' are anagrams: {is_anagram('aacc', 'ccac')}"
    )  # Expected: False

    # Test Case 4
    print(
        f"'railsafety' and 'fairytales' are anagrams: {is_anagram('railsafety', 'fairytales')}"
    )  # Expected: True

    # Test Case 5
    print(
        f"'dormitory' and 'dirtyroom' are anagrams: {is_anagram('dormitory', 'dirtyroom')}"
    )  # Expected: True
