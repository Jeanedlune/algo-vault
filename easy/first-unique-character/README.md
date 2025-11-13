# First Unique Character

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

## Examples

### Example 1
```
Input: "leetcode"
Output: 0
Explanation: 'l' is the first character that appears only once in the string.
```

### Example 2
```
Input: "loveleetcode"
Output: 2
Explanation: 'v' is the first character that appears only once in the string.
```

### Example 3
```
Input: "aabb"
Output: -1
Explanation: No character appears only once in the string.
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters

## Test Cases

1. `"leetcode"` → `0`
2. `"loveleetcode"` → `2`
3. `"aabb"` → `-1`
4. `"z"` → `0`
5. `"aabbccddeeffg"` → `12`

## Target Complexity

- **Time:** O(n) - where n is the length of the string
- **Space:** O(1) - constant extra space (26 letters for English alphabet)
