using System;

namespace AlgoVault.Easy
{
    public static class ReverseIntegerSolution
    {
        // Time: O(k), Space: O(1)
        public static int ReverseInteger(int x)
        {
            const int INT_MIN = int.MinValue;
            const int INT_MAX = int.MaxValue;

            int rev = 0;
            while (x != 0)
            {
                int pop = x % 10;
                x /= 10;
                if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
                if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
                rev = rev * 10 + pop;
            }
            return rev;
        }
    }
}
