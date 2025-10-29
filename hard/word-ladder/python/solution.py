import string
from typing import List, Set
from collections import deque


def word_ladder(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Find the shortest transformation sequence using bidirectional BFS.

    Args:
        begin_word: Starting word
        end_word: Target word
        word_list: List of valid intermediate words

    Returns:
        Length of shortest transformation sequence, or 0 if no path exists

    Time Complexity: O(N * L^2) but with better average performance
    Space Complexity: O(N * L) for queues and visited sets
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    # Two-way BFS: forward from begin_word, backward from end_word
    forward_queue = deque([(begin_word, 1)])
    backward_queue = deque([(end_word, 1)])

    forward_visited = {begin_word: 1}  # word -> level
    backward_visited = {end_word: 1}

    def get_neighbors(word: str) -> Set[str]:
        """Generate all valid neighbor words"""
        neighbors = set()
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                if c != word[i]:
                    next_word = word[:i] + c + word[i + 1 :]
                    if next_word in word_set:
                        neighbors.add(next_word)
        return neighbors

    def bfs_step(queue: deque, visited: dict, other_visited: dict) -> int:
        """
        Perform one level of BFS expansion.
        Returns path length if connection found, 0 otherwise.
        """
        if not queue:
            return 0

        # Process entire current level
        level_size = len(queue)
        for _ in range(level_size):
            current_word, level = queue.popleft()

            for next_word in get_neighbors(current_word):
                # Check if this word connects to the other search
                if next_word in other_visited:
                    return level + other_visited[next_word]

                # Add to current search if not visited
                if next_word not in visited:
                    visited[next_word] = level + 1
                    queue.append((next_word, level + 1))

        return 0

    # Alternate between forward and backward search
    # Always expand the smaller frontier for better performance
    while forward_queue and backward_queue:
        # Expand the smaller frontier first
        if len(forward_queue) <= len(backward_queue):
            result = bfs_step(forward_queue, forward_visited, backward_visited)
        else:
            result = bfs_step(backward_queue, backward_visited, forward_visited)

        if result > 0:
            return result

    return 0


# Original unidirectional BFS for comparison
def word_ladder_original(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """Original unidirectional BFS implementation"""
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        current_word, level = queue.popleft()

        for i in range(len(current_word)):
            for c in string.ascii_lowercase:
                if c == current_word[i]:
                    continue

                next_word = current_word[:i] + c + current_word[i + 1 :]

                if next_word == end_word:
                    return level + 1

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))

    return 0


# Test both implementations
if __name__ == "__main__":
    test_cases = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
        ("hot", "dot", ["hot", "dot"], 2),
        ("a", "c", ["a", "b", "c"], 2),
        ("hit", "cog", ["hot", "hit", "cog"], 0),
        ("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"], 4),
    ]

    print("Testing both implementations:\n")
    all_passed = True

    for i, (begin, end, words, expected) in enumerate(test_cases, 1):
        original = word_ladder_original(begin, end, words)
        bidirectional = word_ladder(begin, end, words)

        status = "✓" if original == bidirectional == expected else "✗"
        if original != expected or bidirectional != expected:
            all_passed = False

        print(f"{status} Test {i}: {begin} -> {end}")
        print(
            f"  Original: {original}, Bidirectional: {bidirectional}, Expected: {expected}"
        )

    if all_passed:
        print("\n✅ All tests passed for both implementations!")
    else:
        print("\n❌ Some tests failed!")
