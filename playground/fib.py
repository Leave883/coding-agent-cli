import sys


def fib(n):
    """返回第 n 个斐波那契数（从 0 开始计数）。"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python fib.py <n>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("参数必须是整数")
        sys.exit(1)
    if n < 0:
        print("参数必须是非负整数")
        sys.exit(1)
    print(fib(n))
