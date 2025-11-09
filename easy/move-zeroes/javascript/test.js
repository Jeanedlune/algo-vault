import { moveZeroes } from './move_zeroes.js';

function testMoveZeroes() {
  const tests = [
    { input: [0, 1, 0, 3, 12], expected: [1, 3, 12, 0, 0] },
    { input: [0, 0, 1], expected: [1, 0, 0] },
    { input: [4, 5, 6], expected: [4, 5, 6] },
    { input: [0, 0, 0], expected: [0, 0, 0] },
    { input: [1, 0, 2, 0, 3, 0], expected: [1, 2, 3, 0, 0, 0] }
  ];

  tests.forEach((test, i) => {
    const arr = [...test.input];
    moveZeroes(arr);
    const passed = JSON.stringify(arr) === JSON.stringify(test.expected);
    console.log(`Test ${i + 1}: ${passed ? '✓' : '✗'} - ${JSON.stringify(arr)}`);
  });
}

testMoveZeroes();
