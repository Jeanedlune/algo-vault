using System.Text.RegularExpressions;

public class Solution {
    public bool IsPalindrome(string s) {
        string sanitized = Regex.Replace(s, "[^a-zA-Z0-9]", "").ToLower();
        int left = 0;
        int right = sanitized.Length - 1;

        while (left < right) {
            if (sanitized[left] != sanitized[right]) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
