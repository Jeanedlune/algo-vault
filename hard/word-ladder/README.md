# Word Ladder

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

In each step of the transformation:
- You must change exactly one letter
- Each transformed word must exist in the word list

## Examples

Input:
```
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
```
Output:
```
5
```
Explanation: hit -> hot -> dot -> dog -> cog (5 words total)

Input:
```
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
```
Output:
```
0
```
Explanation: endWord "cog" is not in wordList, so no transformation possible

## Constraints
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters
- beginWord != endWord
- All the words in wordList are unique

## Test cases (3–5)
- "hit", "cog", ["hot","dot","dog","lot","log","cog"] -> 5
- "hit", "cog", ["hot","dot","dog","lot","log"] -> 0
- "hot", "dot", ["hot","dot"] -> 2
- "a", "c", ["a","b","c"] -> 2
- "hit", "cog", ["hot","hit","cog"] -> 0

## Target complexity
- Time: O(N * L^2) where N = number of words, L = word length
- Space: O(N * L)
