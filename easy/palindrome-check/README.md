# Palindrome Check

Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

## Examples

**Example 1:**

*   **Input:** `s = "racecar"`
*   **Output:** `true`

**Example 2:**

*   **Input:** `s = "hello"`
*   **Output:** `false`

**Example 3:**

*   **Input:** `s = "A man, a plan, a canal: Panama"`
*   **Output:** `true`
*   **Explanation:** After converting to lowercase and removing non-alphanumeric characters, it becomes "amanaplanacanalpanama", which is a palindrome.

## Constraints

*   `1 <= s.length <= 2 * 10^5`
*   `s` consists only of printable ASCII characters.

## Test Cases

1.  `"racecar"` -> `true`
2.  `"madam"` -> `true`
3.  `"hello"` -> `false`
4.  `"A man, a plan, a canal: Panama"` -> `true`
5.  `"Was it a car or a cat I saw?"` -> `true`

## Complexity

*   **Target Time Complexity:** O(n)
*   **Target Space Complexity:** O(1)
