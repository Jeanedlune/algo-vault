using System;

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
    }
}