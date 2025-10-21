def count_vowels(s: str) -> int:
    """Count vowels in a given string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


if __name__ == "__main__":
    tests = ["hello world", "AEIOU", "xyz", "", "ChatGPT rocks!"]
    for t in tests:
        print(f"'{t}' → {count_vowels(t)}")
