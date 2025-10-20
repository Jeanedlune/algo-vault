package sumarray

// SumArray returns the sum of the elements in nums.
// Time: O(n), Space: O(1)
func SumArray(nums []int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    return total
}
