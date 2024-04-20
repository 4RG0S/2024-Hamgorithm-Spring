import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = {}
num = {}

for i in range(n):
    pokemon = input().strip()
    name[pokemon] = i + 1
    num[i + 1] = pokemon

for _ in range(m):
    value = input().strip()
    if str.isdigit(value):
        value = int(value)
        print(num[value])
    else:
        print(name[value])