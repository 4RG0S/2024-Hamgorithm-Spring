import sys

n = int(sys.stdin.readline())

tile = [0 for i in range(10 ** 6)]
tile[1] = 1
tile[2] = 2
for i in range(3, n + 1):
    tile[i] = tile[i - 1] + tile[i - 2]
print(tile[n] % 10007)
