# Factorial

## Problem Statement

Given a non-negative integer `n`, return the factorial of `n`. The factorial of `n` is the product of all positive integers less than or equal to `n`. The factorial of 0 is defined to be 1.

## Examples

**Input:** `n = 5`
**Output:** `120`
**Explanation:** `5! = 5 * 4 * 3 * 2 * 1 = 120`

**Input:** `n = 0`
**Output:** `1`

## Constraints

-   `0 <= n <= 20` (to avoid overflow in standard 64-bit integer types)

## Test Cases

1.  **Input:** `n = 1`
    **Output:** `1`
2.  **Input:** `n = 3`
    **Output:** `6`
3.  **Input:** `n = 10`
    **Output:** `3628800`
4.  **Input:** `n = 13`
    **Output:** `6227020800`

## Time and Space Complexity

-   **Target Time Complexity:** O(n), as we iterate from 1 to n.
-   **Target Space Complexity:** O(1), using a single variable to store the result.