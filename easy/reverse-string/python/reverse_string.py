def reverse_string(s: str) -> str:
    """
    Reverse the given string.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """
    return s[::-1]


if __name__ == "__main__":
    test_cases = [
        ("hello", "olleh"),
        ("Hacktoberfest", "tsefrebotkcaH"),
        ("Python", "nohtyP"),
        ("a", "a"),
        ("", ""),
    ]

    for text, expected in test_cases:
        result = reverse_string(text)
        assert (
            result == expected
        ), f"Failed for '{text}': expected '{expected}', got '{result}'"
    print("All test cases passed.")
