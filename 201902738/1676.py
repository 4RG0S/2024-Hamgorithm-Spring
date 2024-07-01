import sys

N = int(sys.stdin.readline())

res = 1
for i in range(1, N + 1):
    res *= i

count = 0
reserved = list(reversed(str(res)))
for n in reserved:
    if n != '0':
        break
    else:
        count += 1

print(count)
