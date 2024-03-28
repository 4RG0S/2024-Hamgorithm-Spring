from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def main():
    n, k = int(input()), int(input())
    # 0: empty, 1: apple, 2: snake
    board = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[x-1][y-1] = 1
    
    l = int(input())
    move = []
    for _ in range(l):
        x, c = input().split()
        move.append((int(x), c))

    snake = deque([(0, 0)])
    x, y, d, i, second = 0, 0, 0, 0, 0
    while True:
        # 뱀 머리 방향 조정
        if i < l:
            s, c = move[i]
            if second == s:
                if c == 'L':
                    d = (d-1)%4
                elif c == 'D':
                    d = (d+1)%4
                i += 1
        
        # 뱀 머리 이동
        x, y = x + dx[d], y + dy[d]
        snake.append((x, y))
        second += 1
        
        # 뱀 머리 위치에 따른
        if 0 <= x < n and 0 <= y < n:
            if board[x][y] == 0:
                board[x][y] = 2
                tx, ty = snake.popleft()
                board[tx][ty] = 0
            elif board[x][y] == 1:
                board[x][y] = 2
            else:
                break
        else:
            break

    print(second)

if __name__ == "__main__":
    main()