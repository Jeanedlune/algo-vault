# easy/factorial/python/factorial.py


def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Verification block for all test cases from the README
if __name__ == "__main__":
    test_cases = {5: 120, 0: 1, 1: 1, 3: 6, 10: 3628800, 13: 6227020800}

    all_passed = True
    for n, expected in test_cases.items():
        actual = factorial(n)
        if actual == expected:
            print(f"✅ Test case n={n} PASSED")
        else:
            print(f"❌ Test case n={n} FAILED")
            print(f"  - Expected: {expected}")
            print(f"  - Got:      {actual}")
            all_passed = False

    print("\n--------------------")
    if all_passed:
        print("🎉 All tests passed successfully!")
    else:
        print("🔥 Some tests failed.")
    print("--------------------")
