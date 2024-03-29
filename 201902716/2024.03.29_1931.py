import sys

N = int(sys.stdin.readline().rstrip())
times = []

for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().split())))

times.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0

for time in times:
    if time[0] >= end:
        cnt += 1
        end = time[1]

print(cnt)
