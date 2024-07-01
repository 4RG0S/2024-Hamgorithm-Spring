import sys

N = int(sys.stdin.readline().rstrip())
color_paper = []
b_num = 0
w_num = 0

for _ in range(N):
    color_paper.append(list(map(int, sys.stdin.readline().split())))


def divide(x, y, n):
    global b_num
    global w_num

    color = color_paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != color_paper[i][j]:
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return

    if color == 1:
        b_num += 1
    else:
        w_num += 1

divide(0, 0, N)
print(w_num)
print(b_num)
