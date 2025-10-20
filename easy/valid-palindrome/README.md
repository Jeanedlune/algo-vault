# Valid Palindrome

## Problem Statement

Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

## Examples

**Input:** `s = "A man, a plan, a canal: Panama"`
**Output:** `true`
**Explanation:** "amanaplanacanalpanama" is a palindrome.

**Input:** `s = "race a car"`
**Output:** `false`
**Explanation:** "raceacar" is not a palindrome.

## Constraints

-   `1 <= s.length <= 2 * 10^5`
-   `s` consists only of printable ASCII characters.

## Test Cases

1.  **Input:** `"Was it a car or a cat I saw?"`
    **Output:** `true`
2.  **Input:** `"tab a cat"`
    **Output:** `false`
3.  **Input:** `""` (Empty string)
    **Output:** `true`
4.  **Input:** `".,"` (Only non-alphanumeric)
    **Output:** `true`
5.  **Input:** `"ab@a"`
    **Output:** `false`

## Time and Space Complexity

-   **Time Complexity:** O(n), where n is the length of the string. We iterate through the string at most once.
-   **Space Complexity:** O(1), if we modify the string in-place or use pointers. O(n) if we create a new sanitized string. (The two-pointer approach will be O(1)).