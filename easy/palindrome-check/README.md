# Palindrome Check

## Problem Statement

Given a string `s`, return `true` if the string reads the same forwards and backward, and `false` otherwise.

## Examples

**Input:** `s = "racecar"`
**Output:** `true`

**Input:** `s = "hello"`
**Output:** `false`

## Constraints

-   `0 <= s.length <= 2 * 10^5`
-   `s` consists of lowercase English letters.

## Test Cases

1.  **Input:** `s = "madam"`
    **Output:** `true`
2.  **Input:** `s = "level"`
    **Output:** `true`
3.  **Input:** `s = "github"`
    **Output:** `false`
4.  **Input:** `s = "a"`
    **Output:** `true`
5.  **Input:** `s = ""` (Empty string)
    **Output:** `true`

## Time and Space Complexity

-   **Target Time Complexity:** O(n), where n is the length of the string.
-   **Target Space Complexity:** O(1), as we only need a few pointers.