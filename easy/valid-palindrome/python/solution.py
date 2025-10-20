


def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, considering only alphanumeric characters and ignoring cases.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Move the left pointer until it finds an alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1

        # Move the right pointer until it finds an alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        # Move pointers inward
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Test cases from README
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("tab a cat") is False
    assert is_palindrome("") is True
    assert is_palindrome(".,") is True
    # Note: "ab@a" should be True, correcting the README test case
    assert is_palindrome("ab@a") is True
    print("All test cases passed!")
