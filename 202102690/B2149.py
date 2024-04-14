key = list(input())
secret = input()

n = len(key)
table_n = len(secret)//n
table = [[] for _ in range(table_n)]

for i in range(len(secret)) :
    table[i%table_n].append(secret[i])

result = [[0]*n for _ in range(len(table))]
key_sort = sorted(key)

for i, k in enumerate(key) :
    real_index = key_sort.index(k)
    key_sort[real_index] = '*'
    for j in range(len(table)) :
        result[j][i] = table[j][real_index]

answer = ""
for i in range(len(result)) :
    for j in range(n) :
        answer += result[i][j]
print(answer)
