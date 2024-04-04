import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
ans = []
def DFS():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        DFS()
        ans.pop()
        visited[i] = False

DFS()

