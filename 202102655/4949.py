while(True):
    stack = []
    in_str = input()
    if in_str == ".":
        break
    for c in in_str:
        if c == ".":
            if len(stack) == 0:
                print('yes')
            else:
                print('no')
            break
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                print('no')
                break
        elif c == ']':
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                print('no')
                break