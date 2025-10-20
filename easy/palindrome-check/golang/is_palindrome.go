package main

import (
	"regexp"
	"strings"
)

func IsPalindrome(s string) bool {
	re := regexp.MustCompile(`[^a-zA-Z0-9]+`)
	sanitized := strings.ToLower(re.ReplaceAllString(s, ""))

	left, right := 0, len(sanitized)-1
	for left < right {
		if sanitized[left] != sanitized[right] {
			return false
		}
		left++
		right--
	}
	return true
}
