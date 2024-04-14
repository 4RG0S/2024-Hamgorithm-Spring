import math
N = int(input())
a = list(map(int, input().split()))
B, C = map(int, input().split())

result = N

for a_i in a:
    if a_i < B:
        continue
    result += math.ceil((a_i - B) / C)
print(result)