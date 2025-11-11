package trappingrainwater

func TrappingRainWater(height []int) int {
	if len(height) < 3 {
		return 0
	}
	
	left, right := 0, len(height)-1
	leftMax, rightMax := height[left], height[right]
	water := 0
	
	for left < right {
		if leftMax < rightMax {
			left++
			if height[left] < leftMax {
				water += leftMax - height[left]
			} else {
				leftMax = height[left]
			}
		} else {
			right--
			if height[right] < rightMax {
				water += rightMax - height[right]
			} else {
				rightMax = height[right]
			}
		}
	}
	
	return water
}
