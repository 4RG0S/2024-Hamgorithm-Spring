import sys
result = [0]*12
result[1] = 1
result[2] = 2
result[3] = 4
for i in range(4, 12):
    result[i] = result[i-1] + result[i-2] + result[i-3]

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    print(result[a])