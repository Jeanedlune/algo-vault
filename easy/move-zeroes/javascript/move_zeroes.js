export function moveZeroes(nums) {
  let nonZeroPos = 0;

  // Move all non-zero elements to the front
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      nums[nonZeroPos] = nums[i];
      nonZeroPos++;
    }
  }

  // Fill remaining positions with zeros
  for (let i = nonZeroPos; i < nums.length; i++) {
    nums[i] = 0;
  }
}
