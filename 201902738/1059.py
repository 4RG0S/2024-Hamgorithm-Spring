import sys

L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().strip().split(' ')))
n = int(sys.stdin.readline())

res = 0
if n in S:
    print(res)
else:
    S.append(n)
    S.sort()
    idx = S.index(n)
    print("S: ", S)
    if idx == 0:
        for i in range(1, n + 1):
            for j in range(i, S[1]):
                if j >= n and i < j:
                    print(f"i: {i} j: {j}")
                    res += 1

    elif idx == len(S) - 1:
        for i in range(S[idx - 1], n + 1):
            for j in range(i, 1001):
                if j >= n and i < j:
                    print(f"i: {i} j: {j}")
                    res += 1
    else:
        for i in range(S[idx - 1] + 1, n + 1):
            for j in range(i, S[idx + 1]):
                if j >= n and i < j:
                    print(f"i: {i} j: {j}")
                    res += 1
    print(res)
