export const singleNumber = (nums: number[]): number => {
  return nums.reduce((acc, num) => acc ^ num, 0);
};