# Word Ladder

## Problem Statement

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the **number of words** in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

In each step of the transformation:
- You must change **exactly one letter**
- Each transformed word must exist in the word list

## Constraints

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters
- `beginWord != endWord`
- All the words in `wordList` are unique

## Examples

### Example 1: Basic Case
```
Input: 
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: hit -> hot -> dot -> dog -> cog (5 words total)
```

### Example 2: No Path Exists
```
Input:
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: endWord "cog" is not in wordList, so no transformation possible
```

### Example 3: Direct Transformation
```
Input:
  beginWord = "hot"
  endWord = "dot"
  wordList = ["hot","dot"]

Output: 2

Explanation: hot -> dot (2 words total)
```

## Test Cases

| # | beginWord | endWord | wordList | Expected Output |
|---|-----------|---------|----------|-----------------|
| 1 | "hit" | "cog" | ["hot","dot","dog","lot","log","cog"] | 5 |
| 2 | "hit" | "cog" | ["hot","dot","dog","lot","log"] | 0 |
| 3 | "hot" | "dot" | ["hot","dot"] | 2 |
| 4 | "a" | "c" | ["a","b","c"] | 2 |
| 5 | "hit" | "cog" | ["hot","hit","cog"] | 0 |

## Complexity Analysis

- **Time Complexity**: `O(N * L * 26)` 
  - N = number of words in wordList
  - L = length of each word
  - 26 = trying all lowercase letters
  
- **Space Complexity**: `O(N * L)`
  - Queue storage: O(N)
  - Visited set: O(N)
  - Word set: O(N)

## Approach

This problem is solved using **Breadth-First Search (BFS)**:

1. Convert `wordList` to a set for O(1) lookups
2. Use BFS starting from `beginWord`
3. For each word, try changing each character position to all 26 letters
4. If the new word is in `wordList` and not visited, add it to the queue
5. Track the level (distance) at each step
6. Return level when `endWord` is reached
7. Return 0 if queue is exhausted without finding `endWord`

## Implementation

See `solution.py` for the Python implementation.

## Running Tests

```bash
# Run the built-in test harness
python solution.py

# Or use pytest (if installed)
pytest test_solution.py
```