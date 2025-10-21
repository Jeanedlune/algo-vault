# Anagram Check

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

**Input:** `s = "anagram"`, `t = "nagaram"`
**Output:** `true`

**Input:** `s = "rat"`, `t = "car"`
**Output:** `false`

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Test Cases

1.  **Input:** `s = "listen"`, `t = "silent"`
    **Output:** `true`
2.  **Input:** `s = "hello"`, `t = "world"`
    **Output:** `false`
3.  **Input:** `s = "aacc"`, `t = "ccac"`
    **Output:** `false` (Character counts must match)
4.  **Input:** `s = "railsafety"`, `t = "fairytales"`
    **Output:** `true`
5.  **Input:** `s = "dormitory"`, `t = "dirtyroom"`
    **Output:** `true`

## Time and Space Complexity

- **Target Time Complexity:** O(n), where n is the length of the strings.
- **Target Space Complexity:** O(k), where k is the number of unique characters. For a fixed character set like lowercase English letters, this is O(1).
