/**
 * Finds the majority element in an array of numbers.
 *
 * The majority element is the element that appears more than ⌊n / 2⌋ times.
 *
 * @param {number[]} nums - The input array of numbers.
 * @returns {number} The majority element.
 */
export const majorityElement = (nums: number[]): number => {
  let count = 0;
  let candidate: number | null = null;

  for (const num of nums) {
    if (count === 0) {
      candidate = num;
    }
    count += num === candidate ? 1 : -1;
  }

  return candidate!;
};
