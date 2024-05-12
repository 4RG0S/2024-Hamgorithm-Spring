import sys, math

def prim(x):
    if x== 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if x % i == 0:
            return False
    return True

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    while True:
        if prim(n):
            print(n)
            break
        else:
            n+=1