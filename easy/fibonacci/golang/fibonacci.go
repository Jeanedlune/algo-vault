package fibonacci

func Fibonacci(n int) []int {
	if n == 0 {
		return []int{}
	}

	result := make([]int, 0, n)

	if n >= 1 {
		result = append(result, 0)
	}
	if n >= 2 {
		result = append(result, 1)
	}

	for i := 2; i < n; i++ {
		result = append(result, result[i-1]+result[i-2])
	}

	return result
}
