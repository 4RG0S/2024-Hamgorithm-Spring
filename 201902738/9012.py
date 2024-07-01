import sys

T = int(sys.stdin.readline())

for _ in range(T):
    data = list(sys.stdin.readline().strip())
    stack = []

    if len(data) % 2 != 0 or data[0] == ')' or data[-1] == '(':
        print('NO')
        continue

    for d in data:
        if not stack:
            stack.append(d)
        else:
            if stack[-1] == '(' and d == ')':
                stack.pop()
            else:
                stack.append(d)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
