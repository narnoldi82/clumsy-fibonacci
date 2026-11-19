"""Calculate and print the Fibonacci series."""


def print_fibonacci_series(length: int) -> list[int]:
    """Print and return the first ``length`` Fibonacci numbers."""
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")

    series: list[int] = []
    current, following = 0, 1

    for _ in range(length):
        series.append(current)
        current, following = following, current + following

    print("This is the Fibonacci Series (n={})".format((length)))
    print(*series)
    return series


if __name__ == "__main__":
    print_fibonacci_series(10)
