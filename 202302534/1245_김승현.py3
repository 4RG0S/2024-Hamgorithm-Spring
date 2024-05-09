from collections import deque
import sys
input =sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
visited =[[False for _ in range(m)] for _ in range(n)]
q = deque()
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
ans = 0
high =[[] for _ in range(501)]
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue

        tmp = []
        h = a[i][j]
        q.append([i, j])
        visited[i][j] = True
        tmp.append([i,j])
        while q:
            x, y = q.popleft()
            for k in range(8):
                X, Y = x+dx[k], y+dy[k]
                if X < 0 or Y < 0 or X >= n or Y >= m or visited[X][Y]:
                    continue

                if a[X][Y] == h:
                    visited[X][Y] = True
                    q.append([X,Y])
                    tmp.append([X,Y])
        high[h].append(tmp)
for i in range(len(high)):
    for S in high[i]:
        #print(i,S)
        flag = False
        for x,y in S:
            if flag:
                break
            for k in range(8):
                X, Y = x+dx[k], y+dy[k]
                if X < 0 or Y < 0 or X >= n or Y >= m:
                    continue
                if a[X][Y] > i:
                    flag = True
                    break
        if not flag:
            ans += 1

print(ans)