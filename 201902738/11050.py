import sys

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

N, K = map(int, sys.stdin.readline().split())
M = N - K

print(factorial(N) // (factorial(K) * factorial(M)))
