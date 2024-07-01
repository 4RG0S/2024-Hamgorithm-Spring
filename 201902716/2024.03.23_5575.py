import sys

for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, sys.stdin.readline().split())
    s = sh * 3600 + sm * 60 + ss
    e = eh * 3600 + em * 60 + es
    t = e - s
    h = t // 3600
    t %= 3600
    m = t // 60
    t %= 60
    s = t
    print(h, m, s)
