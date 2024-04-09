import sys

N = int(sys.stdin.readline())
time = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    C = B - A
    time.append(C)

time.sort()
if len(time) % 2 == 1:
    print(1)
else:
    half = len(time) // 2
    print(time[half] - time[half - 1] + 1)
