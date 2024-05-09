# 연속해야하는줄 착각
# 감소하는 부분수열 길이 구하는 방법을 잘못 생각함
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dpu = [1] * N # i번째 원소까지 증가하는 부분 수열의 최대 길이
dpd = [1] * N # i번째 원소부터 감소하는 부분 수열의 최대 길이
max_length = 1 # 최대 길이

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            dpu[i] = max(dpu[i], dpu[j] + 1)
    # dpu[i] = dpu[i-1] + 1 if A[i] > A[i-1] else 1

for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            dpd[i] = max(dpd[i], dpd[j] + 1)
    # dpd[i] = dpd[i+1] + 1 if A[i] > A[i+1] else 1
    max_length = max(max_length, dpu[i] + dpd[i] - 1)
# print(dpu)
# print(dpd)
print(max_length)