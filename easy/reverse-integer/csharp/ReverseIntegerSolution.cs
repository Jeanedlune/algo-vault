using System;

namespace AlgoVault.Easy
{
    public static class ReverseIntegerSolution
    {
        // Time: O(k), Space: O(1)
        public static int ReverseInteger(int x)
        {
            const int INT_MIN = -2147483648; // int.MinValue
            const int INT_MAX = 2147483647;  // int.MaxValue

            int sign = x < 0 ? -1 : 1;
            long a = Math.Abs((long)x); // use long during abs to avoid overflow on MinValue
            int rev = 0;
            while (a != 0)
            {
                int digit = (int)(a % 10);
                a /= 10;
                if (rev > (INT_MAX - digit) / 10)
                    return 0;
                rev = rev * 10 + digit;
            }
            rev *= sign;
            if (rev < INT_MIN || rev > INT_MAX) return 0;
            return rev;
        }
    }
}
