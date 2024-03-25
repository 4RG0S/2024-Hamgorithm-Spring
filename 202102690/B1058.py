import copy

n = int(input())
friends = [[0]*n for _ in range(n)]

for i in range(n) :
    tmp = input()
    for j in range(n) :
        if tmp[j] == 'Y' :
            friends[i][j] = 1

twofriends = [[] for _ in range(n)]

for i in range(n) :
    cur = []
    for j in range(n) :
        if friends[j][i] == 1 :
            twofriends[i].append(j)
            twofriends[j].append(i)
            cur.append(j)
    if len(cur) >= 2 :
        for k in cur :
            tmp_cur = copy.deepcopy(cur)
            tmp_cur.remove(k)
            twofriends[k].extend(tmp_cur)
    for j in range(n) :
        twofriends[j] = list(set(twofriends[j]))
result = 0
for i in range(n) :
    if result < len(twofriends[i]) :
        result = len(twofriends[i])

print(result)