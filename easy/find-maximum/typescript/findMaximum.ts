export function findMaximum(nums: number[]): number {
  if (nums.length === 0) {
    throw new Error("Array must not be empty");
  }

  let max = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > max) {
      max = nums[i];
    }
  }
  return max;
}

if (require.main === module) {
  const tests = [
    { nums: [1, 5, 3, 9, 2], expected: 9 },
    { nums: [42], expected: 42 },
    { nums: [-5, -1, -8, -3], expected: -1 },
    { nums: [100, 50, 25, 10], expected: 100 },
    { nums: [7, 9, 3, 9, 1], expected: 9 },
  ];

  tests.forEach((test) => {
    const result = findMaximum(test.nums);
    if (result === test.expected) {
      console.log(`✅ Test passed: [${test.nums}] → ${result}`);
    } else {
      console.log(
        `❌ Test failed: [${test.nums}] → expected ${test.expected}, got ${result}`
      );
    }
  });
}
