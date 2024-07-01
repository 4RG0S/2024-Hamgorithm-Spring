import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort(reverse=True)

max_val = 0
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum = data[i] + data[j] + data[k]
            if sum > M:
                continue
            elif sum == M:
                print(M)
                exit()
            else:
                if max_val < sum:
                    max_val = sum

print(max_val)
