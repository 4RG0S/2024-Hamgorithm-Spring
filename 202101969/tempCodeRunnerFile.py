import sys

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

def check_travel_plan(plan, parents):
    start = find(plan[0], parents)
    for city in plan[1:]:
        if find(city, parents) != start:
            return "NO"  
    return "YES" 

# 입력 처리
n = int(input()) 
m = int(input()) 
parents = [i for i in range(n)]  
for i in range(n):
    link = list(map(int, input().split()))
    for j in range(n):
        if link[j] == 1:
            union(i, j, parents)


plan = list(map(int, input().split()))  
print(check_travel_plan(plan, parents)) 