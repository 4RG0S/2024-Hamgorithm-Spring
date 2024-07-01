import sys

def myRound(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    diff = []
    for _ in range(n):
        diff.append(int(sys.stdin.readline()))

    diff.sort()

    p = myRound(n * 0.15)
    res = 0
    for i in range(p, n - p):
        res += diff[i]
    res /= n - 2 * p
    
    print(myRound(res))
