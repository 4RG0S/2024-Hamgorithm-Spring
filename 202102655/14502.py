from collections import deque
import copy
import sys
input = sys.stdin.readline

d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque()
    #queue에 2의 위치 전부 append
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 2:
                queue.append((i,k))

    while queue:
        r,c = queue.popleft()

        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]

            if (0<=dr<n) and (0<=dc<m):
                if test_map[dr][dc] == 0:
                    test_map[dr][dc] =2
                    queue.append((dr,dc))

    global result
    count = 0
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count +=1

    result = max(result, count)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1
                make_wall(count+1)
                lab_map[i][k] = 0


n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)

print(result)