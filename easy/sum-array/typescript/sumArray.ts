// Sum of Array - TypeScript
// Time: O(n), Space: O(1)

export function sumArray(nums: number[]): number {
  let total = 0;
  for (let i = 0; i < nums.length; i++) total += nums[i];
  return total;
}
