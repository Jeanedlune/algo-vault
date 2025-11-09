def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome considering only alphanumeric characters
    and ignoring cases.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Test cases
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))  # False
    print(is_palindrome("Was it a car or a cat I saw?"))  # True
    print(is_palindrome("tab a cat"))  # False
    print(is_palindrome(""))  # True
    print(is_palindrome(".,"))  # True
    print(is_palindrome("ab@a"))  # True
