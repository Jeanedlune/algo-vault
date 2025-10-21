def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    tests = [0, 1, 2, 5, 7]
    for t in tests:
        print(f"n={t} → {fibonacci(t)}")
