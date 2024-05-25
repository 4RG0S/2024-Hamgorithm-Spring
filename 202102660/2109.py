# 자료구조

import sys

n = int(sys.stdin.readline())
h_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
h_list.sort(key=lambda x: (-x[0], x[1])) # p 큰순, d 작은 순 정렬    

sum = 0
days = [0]*10001
days[0] = 1
for i in range(n):
    (p, d) = h_list[i]
    while d > 1 and days[d] != 0:
        d -= 1
    if days[d] == 0:
        days[d] = 1
        sum += p
    
print(sum)
    
    
    