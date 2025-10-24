package findmaximum

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
