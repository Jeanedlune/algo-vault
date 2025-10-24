using System;
using System.Collections.Generic;

namespace AlgoVault.Easy
{
    public static class FindMaximumSolution
    {
        public static int FindMaximum(int[] nums)
        {
            if (nums == null || nums.Length == 0)
            {
                throw new ArgumentException("Array must not be empty");
            }

            int max = nums[0];
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] > max)
                {
                    max = nums[i];
                }
            }
            return max;
        }

        static void Main()
        {
            var tests = new List<(int[], int)>
            {
                (new int[] { 1, 5, 3, 9, 2 }, 9),
                (new int[] { 42 }, 42),
                (new int[] { -5, -1, -8, -3 }, -1),
                (new int[] { 100, 50, 25, 10 }, 100),
                (new int[] { 7, 9, 3, 9, 1 }, 9),
            };

            foreach (var (nums, expected) in tests)
            {
                int result = FindMaximum(nums);
                if (result == expected)
                {
                    Console.WriteLine($"✅ Test passed: [{string.Join(", ", nums)}] → {result}");
                }
                else
                {
                    Console.WriteLine($"❌ Test failed: [{string.Join(", ", nums)}] → expected {expected}, got {result}");
                }
            }
        }
    }
}