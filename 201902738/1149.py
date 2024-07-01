import sys

N = int(sys.stdin.readline())
RGB = []
PREV = ""

for i in range(N):
    r, g, b = map(int, sys.stdin.readline().strip().split())
    if i == 0:
        RGB.append([r, g, b])
    else:
        RGB.append([r + min(RGB[i - 1][1], RGB[i - 1][2]), 
                    g + min(RGB[i - 1][0], RGB[i - 1][2]), 
                    b + min(RGB[i - 1][0], RGB[i - 1][1])])

print(min(RGB[N - 1]))
