import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

ans = []  # 정답 저장
idx = 0   # 제거 대상 인덱스
for i in range(n):
    idx += k-1
    if idx >= len(arr):   # 인덱스가 범위를 벗어나면
        idx = idx % len(arr)

    ans.append(str(arr.pop(idx)))

print("<", ", ".join(ans), ">", sep="")