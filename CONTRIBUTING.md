# Contributing to algo-vault

Thank you for your interest in contributing. This repository is designed to be beginner-friendly and rigorous.

## How to contribute

1. Pick or open an Issue with labels `hacktoberfest`, `good-first-issue`, or `help-wanted`.
2. Fork the repo, clone your fork, and create a branch:
   - `<difficulty>/<problem-slug>/<language>/<short-desc>`
   - Example: `easy/two-sum/python/hashmap-solution`
3. Implement your solution in the correct directory:
   - `<difficulty>/<problem-slug>/<language>/`
4. Add/verify the problem `README.md`:
   - Statement, I/O examples, constraints, 3–5 test cases, target time/space complexities.
5. Format and lint code. Add tests or minimal verification, if applicable.
6. Commit using Conventional Commits. Open a PR with the template and link the Issue.
7. Address review feedback and iterate until merged.

## Code style (by language)

These are the default style baselines. Use them consistently unless the problem folder specifies otherwise.

### Go

- Format: `go fmt ./...`
- Vet: `go vet ./...`
- Example:

```go
package twosum

func TwoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for i, v := range nums {
        if j, ok := m[target-v]; ok {
            return []int{j, i}
        }
        m[v] = i
    }
    return nil
}
```

### TypeScript

- Lint: `npx eslint .` | Format: `npx prettier --check .` | Type: `npx tsc --noEmit`
- Example:

```ts
export function twoSum(nums: number[], target: number): number[] {
  const idx = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const want = target - nums[i];
    if (idx.has(want)) return [idx.get(want) as number, i];
    idx.set(nums[i], i);
  }
  return [];
}
```

### Python

- Format: `black .` | Lint: `ruff .` | Tests: `pytest`
- Example:

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, v in enumerate(nums):
        w = target - v
        if w in seen:
            return [seen[w], i]
        seen[v] = i
    return []
```

### JavaScript

- Lint: `npx eslint .` | Format: `npx prettier --check .`
- Example:

```js
export function twoSum(nums, target) {
  const idx = new Map();
  for (let i = 0; i < nums.length; i++) {
    const want = target - nums[i];
    if (idx.has(want)) return [idx.get(want), i];
    idx.set(nums[i], i);
  }
  return [];
}
```

### C#

- Build/format: `dotnet build -c Release` / `dotnet format`
- Example:

```csharp
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
```

### C++

- Standard: C++17 | Prefer `std::vector`, `std::unordered_map`
- Example:

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int,int> m;
    for (int i = 0; i < (int)nums.size(); ++i) {
        int want = target - nums[i];
        auto it = m.find(want);
        if (it != m.end()) return {it->second, i};
        m[nums[i]] = i;
    }
    return {};
}
```

## Commit messages

Use Conventional Commits:

- `feat(ts): implement two-sum`
- `test(py): add edge cases for two-sum`
- `docs: add problem README for binary-search`
- `chore(go): run fmt and vet`

## Testing requirements

- Each implementation should include 3–5 test cases (README or a test file).
- Cover typical, edge, and negative scenarios.
- Target optimal time/space complexity as stated in the problem README.

## Review process

- Maintainers review for correctness, clarity, style, and tests.
- Requested changes should be addressed promptly.
- Merging occurs after approvals and passing checks.

## Branching and PRs

- Branch naming: `<difficulty>/<problem>/<language>/<short-desc>`
- Open PRs that:
  - Link the Issue and explain the approach
  - Include complexity analysis
  - Pass formatters/linters
