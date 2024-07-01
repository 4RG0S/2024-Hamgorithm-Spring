import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
accumulated_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

def solution(x1, y1, x2, y2):
    # 1. 누적 합 구하기
    # 2. 누적 합 구간 빼기
    result = accumulated_sum[x2][y2] - accumulated_sum[x1-1][y2] - accumulated_sum[x2][y1-1] + accumulated_sum[x1-1][y1-1]
    print(result)

def calc_acc_sum():
    global accumulated_sum
    for row in range(1, n+1):
        for col in range(1, n+1):
            accumulated_sum[row][col] = graph[row-1][col-1] + accumulated_sum[row-1][col] + accumulated_sum[row][col-1] - accumulated_sum[row-1][col-1]

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

calc_acc_sum()
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    solution(x1, y1, x2, y2)