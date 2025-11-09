package containsduplicate

import "testing"

func TestContainsDuplicate(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected bool
	}{
		{"has duplicate", []int{1, 2, 3, 1}, true},
		{"no duplicate", []int{1, 2, 3, 4}, false},
		{"multiple duplicates", []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
		{"empty array", []int{}, false},
		{"single element", []int{42}, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := ContainsDuplicate(tt.nums)
			if result != tt.expected {
				t.Errorf("ContainsDuplicate(%v) = %v, want %v", tt.nums, result, tt.expected)
			}
		})
	}
}
