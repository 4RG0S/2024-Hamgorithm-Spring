str = input()
stack = []

answer = 0
temp = 1
for i, char in enumerate(str):
    if char == '(':
        temp *= 2
        stack.append('(')
    elif char == '[':
        temp *= 3
        stack.append('[')
    elif char == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if str[i-1] == '(':
            answer += temp
        temp //= 2
        stack.pop()
    elif char == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if str[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    answer = 0

print(answer)
