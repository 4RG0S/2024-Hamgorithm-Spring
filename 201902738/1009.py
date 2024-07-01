import sys

def power(k, n):
    result = 1
    while n > 0:        
        if n % 2 == 1:
            result = (result * k) % 10
        n //= 2
        k = k * k % 10

    return result

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    c = power(a, b)
    print(10 if c == 0 else c)
