import sys

N, S, P = map(int, sys.stdin.readline().strip().split())
tmp = 0
if N != 0:
    Scores = list(map(int, sys.stdin.readline().strip().split()))
    Scores.append(S)
    Scores.sort(reverse=True)
    tmp = Scores.index(S) + 1
    dup = Scores.count(S)
    if tmp + dup - 1 > P:
        print(-1)
    else:
        print(tmp)
else:
    print(1)
