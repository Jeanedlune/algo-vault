# algo-vault Style Guide for Code Review

This repository is a Hacktoberfest-friendly multi-language Algorithms & Data Structures collection. When reviewing code, please focus on the following guidelines:

## Repository Structure

- All algorithm solutions must be placed in the correct directory: `<difficulty>/<problem-slug>/<language>/`
- Each problem must have a `README.md` with:
  - Clear problem statement
  - Input/Output examples (minimum 3)
  - Constraints
  - 3-5 test cases
  - Target time complexity
  - Target space complexity

## Language-Specific Guidelines

### Go
- Use `go fmt` for formatting
- Run `go vet` for static analysis
- Prefer `CamelCase` for exported names, `mixedCaps` for internal
- Use table-driven tests when applicable
- Avoid naked returns in functions longer than a few lines
- Check for error handling - don't ignore errors

### TypeScript
- Use strict typing (`--strict` mode)
- Prefer named exports over default exports
- Use descriptive type names and interfaces
- Avoid `any` type unless absolutely necessary
- Use readonly for immutable data
- Prefer `const` over `let`, never use `var`

### Python
- Follow PEP 8 style guide
- Use type hints for function signatures
- Format with Black (line length 88)
- Use descriptive variable names (no single letters except loop counters)
- Prefer list comprehensions over map/filter when readable
- Use `pytest` for testing

### JavaScript
- Use ESLint with Standard or Airbnb style
- Prefer `const` and `let` over `var`
- Use arrow functions for callbacks
- Use template literals for string interpolation
- Avoid global variables
- Use strict equality (`===`) not loose equality (`==`)

### C#
- Follow Microsoft's C# coding conventions
- Use PascalCase for public members, camelCase for private
- Use file-scoped namespaces
- Prefer `var` when type is obvious from right side
- Use nullable reference types
- Run `dotnet format` before committing

### C++
- Use C++17 standard
- Prefer STL containers over raw arrays
- Use RAII principles (avoid manual new/delete)
- Prefer `std::vector` over arrays
- Use `const` correctness
- Avoid `using namespace std;` in headers
- Use `auto` when type is obvious and improves readability

## Algorithm Implementation Requirements

### Correctness
- Solutions must handle all test cases in the problem README
- Edge cases must be considered (empty input, single element, negative numbers, etc.)
- No hardcoded solutions - algorithms must be general-purpose
- Return types must match the problem specification

### Efficiency
- Target the optimal time complexity stated in problem README
- Avoid nested loops when O(n) solution exists
- Use appropriate data structures (HashMap for O(1) lookups, etc.)
- Avoid unnecessary string concatenation in loops
- Don't compute the same value multiple times

### Code Quality
- Functions should be small and focused (single responsibility)
- Use meaningful variable names (no `x`, `temp`, `foo` unless contextually clear)
- Add comments only when code intent is not obvious
- Avoid deep nesting (max 3-4 levels)
- No commented-out code in final submission
- No console.log/print statements in production code (use tests instead)

### Testing
- Each implementation should be verifiable against the test cases in README
- Contributors should manually verify their solution works before submitting
- When possible, include a simple test harness or assertion checks

## Specific Anti-Patterns to Flag

### Security Issues
- Never hardcode sensitive data (API keys, passwords)
- Validate all external input
- Avoid eval() or equivalent in any language
- Use parameterized queries if database operations are involved

### Common Mistakes
- Off-by-one errors in loops
- Integer overflow (especially in languages without big integers)
- Modifying input arrays when not required
- Not handling null/None/nil inputs
- Using wrong comparison operators (`=` vs `==`)

## PR Expectations

- Each PR should target one algorithm or one language implementation
- Branch naming: `<difficulty>/<problem-slug>/<language>/<description>`
- Commit messages should follow Conventional Commits:
  - `feat(ts): implement two-sum`
  - `test(py): add edge cases for fizzbuzz`
  - `docs: update README for palindrome-check`
- PRs must link to the related Issue
- Code must pass linters/formatters for the language
- No merge commits (rebase before submitting)

## Tone and Communication

- Be constructive and encouraging (this is a learning repository)
- Focus on teaching, not just pointing out errors
- Provide examples when suggesting improvements
- Acknowledge good practices when present
- Remember: many contributors are beginners learning algorithms

## Review Priorities

1. **Correctness** - Does the solution work for all test cases?
2. **Complexity** - Does it meet the target O(n) time/space goals?
3. **Readability** - Can other developers understand this code easily?
4. **Style** - Does it follow language-specific conventions?
5. **Tests** - Are edge cases considered?

When a solution is functionally correct but has style issues, approve with suggestions rather than blocking. Encourage iterative improvement.
