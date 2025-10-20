// Reverse Integer - JavaScript implementation
// Time: O(k), Space: O(1)

export function reverseInteger(x) {
  const INT_MIN = -2147483648;
  const INT_MAX = 2147483647;

  let sign = x < 0 ? -1 : 1;
  x = Math.abs(x);
  let rev = 0;

  while (x !== 0) {
    const digit = x % 10;
    x = Math.trunc(x / 10);
    // Check overflow before applying
    if (rev > Math.trunc((INT_MAX - digit) / 10)) return 0;
    rev = rev * 10 + digit;
  }

  rev *= sign;
  if (rev < INT_MIN || rev > INT_MAX) return 0;
  return rev;
}

// Quick manual run when executed directly (Node ESM required)
if (typeof process !== 'undefined' && process.argv[1] && process.argv[1].endsWith('reverseInteger.js')) {
  const cases = [123, -123, 120, 0, 1534236469];
  for (const c of cases) console.log(c, '->', reverseInteger(c));
}
