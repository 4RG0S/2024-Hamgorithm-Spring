import sys

N = int(sys.stdin.readline())
for i in range(N):
    line = sys.stdin.readline().rstrip()
    print("{}. {}".format(i + 1, line))
