from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    singer = [set() for _ in range(n+1)]
    coef = [0 for _ in range(n+1)]
    for _ in range(m):
        seq = list(map(int, input().split()))
        for i in range(1, seq[0]):
            if seq[i+1] in singer[seq[i]]:
                continue
            singer[seq[i]].add(seq[i+1])
            coef[seq[i+1]] += 1
    
    que = deque()
    for i in range(1, n+1):
        if coef[i]:
            continue
        que.append(i)

    seq = []
    while que:
        e = que.popleft()
        seq.append(e)
        for child in singer[e]:
            coef[child] -= 1
            if coef[child]:
                continue
            que.append(child)
    
    if len(seq) == n:
        for i in seq:
            print(i)
    else:
        print(0)
    
if __name__ == "__main__":
    main()