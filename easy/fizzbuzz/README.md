# FizzBuzz

## Problem Statement

Given an integer `n`, return a list of strings where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

The list should be for numbers from 1 to `n`.

## Examples

**Input:** `n = 3`
**Output:** `["1", "2", "Fizz"]`

**Input:** `n = 5`
**Output:** `["1", "2", "Fizz", "4", "Buzz"]`

**Input:** `n = 15`
**Output:** `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`

## Constraints

- `1 <= n <= 10^4`

## Test Cases

1.  **Input:** `n = 1`
    **Output:** `["1"]`
2.  **Input:** `n = 2`
    **Output:** `["1", "2"]`
3.  **Input:** `n = 6`
    **Output:** `["1", "2", "Fizz", "4", "Buzz", "Fizz"]`
4.  **Input:** `n = 10`
    **Output:** `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]`

## Time and Space Complexity

- **Target Time Complexity:** O(n), as we iterate from 1 to n.
- **Target Space Complexity:** O(n), to store the resulting list of strings.
