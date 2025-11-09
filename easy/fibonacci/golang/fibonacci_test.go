package fibonacci

import (
	"reflect"
	"testing"
)

func TestFibonacci(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected []int
	}{
		{"n=0", 0, []int{}},
		{"n=1", 1, []int{0}},
		{"n=2", 2, []int{0, 1}},
		{"n=5", 5, []int{0, 1, 1, 2, 3}},
		{"n=7", 7, []int{0, 1, 1, 2, 3, 5, 8}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := Fibonacci(tt.n)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("Fibonacci(%d) = %v, want %v", tt.n, result, tt.expected)
			}
		})
	}
}
