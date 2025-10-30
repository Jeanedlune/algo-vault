import pytest
from solution import word_ladder


class TestWordLadder:
    """Test suite for Word Ladder problem"""

    def test_basic_case(self):
        """Test basic transformation sequence"""
        result = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        assert result == 5

    def test_no_path_end_word_missing(self):
        """Test when endWord is not in wordList"""
        result = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        assert result == 0

    def test_direct_transformation(self):
        """Test direct one-step transformation"""
        result = word_ladder("hot", "dot", ["hot", "dot"])
        assert result == 2

    def test_single_character_words(self):
        """Test with single character words"""
        result = word_ladder("a", "c", ["a", "b", "c"])
        assert result == 2

    def test_no_valid_path(self):
        """Test when no valid transformation path exists"""
        result = word_ladder("hit", "cog", ["hot", "hit", "cog"])
        assert result == 0

    def test_longer_sequence(self):
        """Test with longer transformation sequence"""
        result = word_ladder(
            "red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
        )
        assert result == 4  # red -> ted -> tex -> tax

    def test_same_length_requirement(self):
        """Test with three-letter words"""
        result = word_ladder("hot", "dog", ["hot", "dot", "dog"])
        assert result == 3  # hot -> dot -> dog


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
