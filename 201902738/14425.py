import sys

N, M = map(int, sys.stdin.readline().strip().split())

str_list = {}

for _ in range(N):
    str_list[sys.stdin.readline().strip()] = 1

count = 0
for _ in range(M):
    input = sys.stdin.readline().strip()
    if input in str_list:
        count += 1

print(count)
