N, M = map(int, input().split())
chess = []
for _ in range(N):
    chess.append(list(input()))
min_cnt = 10000000
for i in range(N-8+1):
    for j in range(M-8+1):
        check_wb = False
        cnt = 0
        cnt_reverse = 0
        if chess[i][j] == 'B':
            check_wb = True
        for x in range(8):
            for y in range(8):
                if (chess[i+x][j+y] == 'W' and check_wb) or (chess[i+x][j+y] == 'B' and not check_wb):
                    cnt += 1
                elif (chess[i+x][j+y] == 'W' and not check_wb) or (chess[i+x][j+y] == 'B' and check_wb):
                    cnt_reverse += 1
                if y != 7:
                    check_wb = not check_wb
        min_cnt = min(min_cnt, cnt_reverse)
        min_cnt = min(min_cnt, cnt)
print(min_cnt)
