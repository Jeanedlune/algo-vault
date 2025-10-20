package golang

// MajorityElement finds the element that appears more than n/2 times.
// It uses the Boyer-Moore Voting Algorithm.
func MajorityElement(nums []int) int {
	count := 0
	var candidate int

	for _, num := range nums {
		if count == 0 {
			candidate = num
		}
		if num == candidate {
			count++
		} else {
			count--
		}
	}

	return candidate
}