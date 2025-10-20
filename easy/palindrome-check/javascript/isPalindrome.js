/**
 * @param {string} s
 * @return {boolean}
 */
export const isPalindrome = (s) => {
  const sanitized = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  let left = 0;
  let right = sanitized.length - 1;

  while (left < right) {
    if (sanitized[left] !== sanitized[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
};
