import sys

N, M = map(int, sys.stdin.readline().strip().split())

people = {}
for _ in range(N):
    people[sys.stdin.readline().strip()] = 0

count = 0
for _ in range(M):
    name = sys.stdin.readline().strip()
    if name in people:
        people[name] += 1
        count += 1
        
people = sorted(people.items(), key=lambda x: x[0])
print(count)
for k, v in people:
    if v > 0:
        print(k)
