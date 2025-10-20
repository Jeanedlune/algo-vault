# FizzBuzz

## Problem Statement

Given an integer `n`, return a list of strings where:
- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

The list should be for numbers from 1 to `n`.

## Input/Output Examples

- **Example 1:**
  - **Input:** `n = 3`
  - **Output:** `["1", "2", "Fizz"]`

- **Example 2:**
  - **Input:** `n = 5`
  - **Output:** `["1", "2", "Fizz", "4", "Buzz"]`

- **Example 3:**
  - **Input:** `n = 15`
  - **Output:** `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`

## Constraints

- `1 <= n`

## Test Cases

- `n = 1` -> `["1"]`
- `n = 2` -> `["1", "2"]`
- `n = 7` -> `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]`
- `n = 10` -> `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]`

## Target Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) (to store the resulting list)
