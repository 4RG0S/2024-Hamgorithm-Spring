import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

ans = [0,0]
for i in range(n):
    leng_r,leng_c = 0,0
    for j in range(n):
        # 가로
        if board[i][j] == '.':
            leng_r+=1
        else:
            leng_r=0
        if leng_r==2:
            ans[0] += 1
        
        # 세로
        if board[j][i] == '.':
            leng_c+=1
        else:
            leng_c=0
        if leng_c==2:
            ans[1] += 1
print(*ans)