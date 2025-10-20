/**
 * @param {number[]} nums
 * @return {number}
 */
export const singleNumber = (nums) => {
  return nums.reduce((acc, num) => acc ^ num, 0);
};