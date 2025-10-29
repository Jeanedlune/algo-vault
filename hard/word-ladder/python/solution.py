import string
from typing import List
from collections import deque


def word_ladder(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Find the shortest transformation sequence from begin_word to end_word.

    Args:
        begin_word: Starting word
        end_word: Target word
        word_list: List of valid intermediate words

    Returns:
        Length of shortest transformation sequence, or 0 if no path exists

    Time Complexity: O(N * L^2) where N is number of words, L is word length
    Space Complexity: O(N * L) for queue and visited set
    """
    # If end_word not in word_list, no transformation possible
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    # BFS: queue stores (current_word, level)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        current_word, level = queue.popleft()

        # Try changing each character position
        for i in range(len(current_word)):
            # Try all 26 lowercase letters
            for c in string.ascii_lowercase:
                # Skip if same character
                if c == current_word[i]:
                    continue

                # Create new word with one character changed
                next_word = current_word[:i] + c + current_word[i + 1 :]

                # Check if we reached the end word
                if next_word == end_word:
                    return level + 1

                # If valid word and not visited, add to queue
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))

    # No transformation sequence found
    return 0


# Test harness for quick verification
if __name__ == "__main__":
    # Test case 1: Basic case
    assert word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    print("✓ Test 1 passed: Basic case")

    # Test case 2: No path exists (end_word not in list)
    assert word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("✓ Test 2 passed: No path exists")

    # Test case 3: Direct transformation
    assert word_ladder("hot", "dot", ["hot", "dot"]) == 2
    print("✓ Test 3 passed: Direct transformation")

    # Test case 4: Single character words
    assert word_ladder("a", "c", ["a", "b", "c"]) == 2
    print("✓ Test 4 passed: Single character")

    # Test case 5: No valid path in list
    assert word_ladder("hit", "cog", ["hot", "hit", "cog"]) == 0
    print("✓ Test 5 passed: No valid path")

    print("\n✅ All tests passed!")
