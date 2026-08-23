import sys


def fib(n):
    """Return the nth Fibonacci number (F(0)=0, F(1)=1)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fib.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: n must be an integer")
        sys.exit(1)

    if n < 0:
        print("Error: n must be >= 0")
        sys.exit(1)

    print(fib(n))
