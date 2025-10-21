# easy/fizzbuzz/python/fizzbuzz.py
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Generates the FizzBuzz sequence up to n.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# Verification block for simple testing
if __name__ == "__main__":
    print(f"FizzBuzz for n=15: {fizzbuzz(15)}")
