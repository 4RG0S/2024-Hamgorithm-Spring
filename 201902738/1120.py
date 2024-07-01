import sys

def check_diff(A, B):
    res = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            res += 1
    return res

A, B = sys.stdin.readline().strip().split(' ')

min_res = 51
for i in range(0, len(B)-len(A) + 1):
    res = check_diff(A, B[i:i+len(A)])
    if res < min_res:
        min_res = res
print(min_res)
