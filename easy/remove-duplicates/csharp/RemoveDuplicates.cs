using System.Collections.Generic;

namespace AlgoVault.Easy
{
    public static class RemoveDuplicates
    {
        public static int[] RemoveDuplicatesFromSorted(int[] nums)
        {
            if (nums.Length == 0)
            {
                return System.Array.Empty<int>();
            }

            var result = new List<int> { nums[0] };

            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] != nums[i - 1])
                {
                    result.Add(nums[i]);
                }
            }

            return result.ToArray();
        }
    }
}
