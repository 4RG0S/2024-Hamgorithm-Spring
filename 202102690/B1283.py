n = int(input())
options = [input() for _ in range(n)]
result = []
used = [" "]

for i in range(n) :
    cur_result = ""
    cur_words = options[i].split(' ')
    complete = False
    for j in range(len(cur_words)) :
        if cur_words[j][0] not in used :
            cur_result += '['+cur_words[j][0]+']'+cur_words[j][1:]
            for k in range(j+1, len(cur_words)) :
                cur_result += " " + cur_words[k]
            used.append(cur_words[j][0].upper())
            used.append(cur_words[j][0].lower())
            complete = True
            break
        else :
            cur_result += cur_words[j] + " "

    if complete == True :
        result.append(cur_result)
        continue

    cur_result = ""
    for j in range(len(options[i])) :
        if options[i][j] not in used :
            cur_result += '['+options[i][j]+']'+options[i][j+1:]
            used.append(options[i][j].upper())
            used.append(options[i][j].lower())
            break
        else :
            cur_result += options[i][j]
    result.append(cur_result)

for i in result :
    print(i)