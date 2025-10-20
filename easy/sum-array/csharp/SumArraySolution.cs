using System;

namespace AlgoVault.Easy
{
    public static class SumArraySolution
    {
        // Time: O(n), Space: O(1)
        public static int SumArray(int[] nums)
        {
            int total = 0;
            for (int i = 0; i < nums.Length; i++) total += nums[i];
            return total;
        }
    }
}
