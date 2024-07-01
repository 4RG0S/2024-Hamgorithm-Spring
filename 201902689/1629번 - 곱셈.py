import sys
input = sys.stdin.readline

a, b, mod = map(int, input().split())

def fast_pow(a, n):
    if n == 1:
        return a % mod
    else:
        x = fast_pow(a, n//2)
        if n % 2 == 0:
            return (x * x) % mod
        else:
            return (x * x * a) % mod
result = fast_pow(a, b)

print(result)
