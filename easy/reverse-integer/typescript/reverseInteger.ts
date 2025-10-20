// Reverse Integer - TypeScript implementation
// Time: O(k), Space: O(1)

export function reverseInteger(x: number): number {
  const INT_MIN = -2147483648;
  const INT_MAX = 2147483647;

  const sign = x < 0 ? -1 : 1;
  x = Math.abs(Math.trunc(x));
  let rev = 0;

  while (x !== 0) {
    const digit = x % 10;
    x = Math.trunc(x / 10);
    if (rev > Math.trunc((INT_MAX - digit) / 10)) return 0;
    rev = rev * 10 + digit;
  }

  rev *= sign;
  if (rev < INT_MIN || rev > INT_MAX) return 0;
  return rev;
}
