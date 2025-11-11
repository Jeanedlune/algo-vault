package validpalindrome

import "unicode"

func IsPalindrome(s string) bool {
	left, right := 0, len(s)-1

	for left < right {
		for left < right && !isAlphanumeric(s[left]) {
			left++
		}
		for left < right && !isAlphanumeric(s[right]) {
			right--
		}

		if left < right {
			if unicode.ToLower(rune(s[left])) != unicode.ToLower(rune(s[right])) {
				return false
			}
			left++
			right--
		}
	}

	return true
}

func isAlphanumeric(c byte) bool {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')
}
