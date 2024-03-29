import sys

N = sys.stdin.readline().rstrip()
l = len(N)

for i in range(l // 10 + (1 if l % 10 != 0 else 0)):
    print(N[i*10:i*10+10])
