import sys

T = int(sys.stdin.readline())

data = []
for _ in range(0, T):
    A, B = sys.stdin.readline().strip().split(' ')
    data.append([int(A), B])

sort_data = sorted(data, key=lambda x: x[0])

for k, v in sort_data:
    print(k, v)
