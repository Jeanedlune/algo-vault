def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Verification block for all test cases from the README
if __name__ == "__main__":
    test_cases = {
        "madam": True,
        "level": True,
        "github": False,
        "a": True,
        "": True,
        "racecar": True,
        "hello": False,
    }

    all_passed = True
    for input_str, expected in test_cases.items():
        actual = is_palindrome(input_str)
        if actual == expected:
            print(f"✅ Test case '{input_str}' PASSED")
        else:
            print(f"❌ Test case '{input_str}' FAILED")
            print(f"  - Expected: {expected}")
            print(f"  - Got:      {actual}")
            all_passed = False

    print("\n--------------------")
    if all_passed:
        print("🎉 All tests passed successfully!")
    else:
        print("🔥 Some tests failed.")
    print("--------------------")
