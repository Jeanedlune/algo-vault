import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, considering only alphanumeric
    characters and ignoring cases.

    This implementation uses a two-pointer approach after sanitizing the
    string. One pointer starts from the beginning, and the other from the end.
    They move towards each other, and if the characters they point to are
    different at any point, the string is not a palindrome.

    Args:
        s: The input string.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    # Sanitize the string: lowercase and keep only alphanumeric characters
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # Two-pointer check
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
