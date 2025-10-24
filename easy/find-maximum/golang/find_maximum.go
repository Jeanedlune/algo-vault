package main

import (
	"fmt"
)

// FindMaximum returns the maximum element in the array
func FindMaximum(nums []int) int {
	if len(nums) == 0 {
		panic("array must not be empty")
	}

	max := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > max {
			max = nums[i]
		}
	}
	return max
}

func main() {
	tests := []struct {
		nums     []int
		expected int
	}{
		{[]int{1, 5, 3, 9, 2}, 9},
		{[]int{42}, 42},
		{[]int{-5, -1, -8, -3}, -1},
		{[]int{100, 50, 25, 10}, 100},
		{[]int{7, 9, 3, 9, 1}, 9},
	}

	for _, test := range tests {
		result := FindMaximum(test.nums)
		if result == test.expected {
			fmt.Printf("✅ Test passed: %v → %d\n", test.nums, result)
		} else {
			fmt.Printf("❌ Test failed: %v → expected %d, got %d\n", test.nums, test.expected, result)
		}
	}
}
