using System.Collections.Generic;

namespace AlgoVault.Easy
{
    public static class TwoSumSolution
    {
        public static int[] TwoSum(int[] nums, int target)
        {
            var map = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++)
            {
                int want = target - nums[i];
                if (map.TryGetValue(want, out int j)) return new[] { j, i };
                map[nums[i]] = i;
            }
            return System.Array.Empty<int>();
        }
    }
}
