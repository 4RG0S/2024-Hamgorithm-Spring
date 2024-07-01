import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10000
for i in range(n):
    arr[i] = int(input())

mem = [0] * 10000
mem[0] = arr[0]
mem[1] = arr[1] + arr[0]
mem[2] = max(mem[0] + arr[2], arr[1] + arr[2], mem[1])
for i in range(3, n):
    mem[i] = max(mem[i - 2] + arr[i], mem[i - 3] + arr[i - 1] + arr[i], mem[i - 1])
print(max(mem))
"""
6
6
10
13
9
8
1
"""