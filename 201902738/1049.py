import sys

N, M = map(int, sys.stdin.readline().split())

S = 1000
O = 1000
for i in range(M):
    line_s, line_o = map(int, sys.stdin.readline().split())
    if line_s > line_o * 6:
        line_s = line_o * 6
    if S > line_s:
        S = line_s
    if O > line_o:
        O = line_o

if S > O * 6:
    S = O * 6

print(S * (N // 6) + min(S ,O * (N % 6)))
