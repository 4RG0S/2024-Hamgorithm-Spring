import sys

N = int(sys.stdin.readline())

hw = []
visit = [False] * 1001

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    hw.append((d, w))

hw.sort(key = lambda x: x[1], reverse=True)
answer = 0

for day, worth in hw:
    i = day
    while i > 0 and visit[i]:
        i -= 1
    if i == 0:
        continue
    else:
        visit[i] = True
        answer += worth

print(answer)