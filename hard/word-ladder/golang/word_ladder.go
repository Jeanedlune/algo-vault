package wordladder

func LadderLength(beginWord string, endWord string, wordList []string) int {
	wordSet := make(map[string]bool)
	for _, word := range wordList {
		wordSet[word] = true
	}

	if !wordSet[endWord] {
		return 0
	}

	beginSet := make(map[string]bool)
	endSet := make(map[string]bool)
	visited := make(map[string]bool)

	beginSet[beginWord] = true
	endSet[endWord] = true
	level := 1

	for len(beginSet) > 0 && len(endSet) > 0 {
		if len(beginSet) > len(endSet) {
			beginSet, endSet = endSet, beginSet
		}

		nextSet := make(map[string]bool)

		for word := range beginSet {
			for i := 0; i < len(word); i++ {
				for c := 'a'; c <= 'z'; c++ {
					if byte(c) == word[i] {
						continue
					}

					newWord := word[:i] + string(c) + word[i+1:]

					if endSet[newWord] {
						return level + 1
					}

					if wordSet[newWord] && !visited[newWord] {
						visited[newWord] = true
						nextSet[newWord] = true
					}
				}
			}
		}

		beginSet = nextSet
		level++
	}

	return 0
}
