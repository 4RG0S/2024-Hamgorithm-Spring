import sys

N, M  = map(int, sys.stdin.readline().strip().split(' '))
s = min(N, M)
rect = []
for _ in range(N):
    num = sys.stdin.readline().strip()
    rect.append(list(map(int, num)))
res = 1
if s != 1:
    for i in range(N):
        for j in range(M):
            n = rect[i][j]
            for k in range(1, s):
                if i + k < N and j + k < M:
                    if n == rect[i+k][j] == rect[i][j+k] == rect[i+k][j+k]:
                        print("i:", i, "j:", j, "k:", k)
                        res = max(res, (k + 1) ** 2)
                        

print(res)
