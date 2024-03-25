a_str, b_str = map(str, input().split())

result = 0

if len(a_str) != len(b_str) :
    print(0)
else :
    for i in range(len(a_str)) :
        if a_str[i] == b_str[i] :
            if a_str[i] == '8' :
                result += 1
        else:
            break
    print(result)