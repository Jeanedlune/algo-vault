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
    print(f"'listen' and 'silent' are anagrams: {is_anagram('listen', 'silent')}")
    print(f"'rat' and 'car' are anagrams: {is_anagram('rat', 'car')}")
