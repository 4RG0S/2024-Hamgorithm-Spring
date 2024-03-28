import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

d = dict()
for num in N_list:
    d[num] = 0
for j in M_list:
    if j in d:
        print(1, end=" ")
    else:
        print(0, end=" ")