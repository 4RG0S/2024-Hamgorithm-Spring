n = int(input())
weight = []

for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)
max_weight = 0
for i in range(n):
    tmp = weight[i] * (i + 1)
    if tmp > max_weight:
        max_weight = tmp
print(max_weight)