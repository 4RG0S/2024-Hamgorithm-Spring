import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

diction = dict()

for num in N_list:
    if num in diction:
        diction[num] = diction[num]+1
    else:
        diction[num] = 1

for c in M_list:
    if c in diction:
        print(diction[c], end=" ")
    else:
        print(0, end= " ")