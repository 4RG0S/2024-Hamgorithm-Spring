import sys
input = sys.stdin.readline
from collections import deque

def execute(func, n, arr):
    op_len = len(func)
    reverse_num = 0

    for num in range(op_len):
        op = func[num]
        if op == "R":
            reverse_num += 1
        elif op == "D":
            if len(arr) < 1:
                return "error"
            else:
                if reverse_num & 1: # 홀수 (reverse)
                    arr.pop()
                else:
                    arr.popleft()
        else:
            return "error"

    if reverse_num & 1:
        arr.reverse()

    return "[" + ",".join(arr) + "]"

t = int(input())

for _ in range(t):
    func = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        arr = deque()
    print(execute(func, n, arr))
