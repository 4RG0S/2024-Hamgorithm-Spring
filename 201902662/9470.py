import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        k, m, p = map(int, input().split())

        parents = [[] for _ in range(m+1)]
        childCnt = [0 for _ in range(m+1)]
        for _ in range(p):
            a, b = map(int, input().split())
            parents[a].append(b)
            childCnt[b] += 1

        strahler = [(0, 0) for _ in range(m+1)]
        
        que = []
        for i in range(1, m+1):
            if childCnt[i] == 0:
                que.append(i)
                strahler[i] = (1, 0)

        while que:
            e = que.pop()
            for p in parents[e]:
                childCnt[p] -= 1
                if childCnt[p] == 0:
                    que.append(p)
                
                a, b = strahler[e][0], strahler[p][0]
                if a > b:
                    strahler[p] = (a, 1)
                elif a == b:
                    if strahler[p][1]:
                        strahler[p] = (a+1, 0)
                    else:
                        strahler[p] = (a, 1)

        print(k, strahler[m][0])

if __name__ == "__main__":
    main()