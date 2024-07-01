import sys

N = int(sys.stdin.readline())

people = {}
for _ in range(N):
    name, option = sys.stdin.readline().strip().split()
    if option == 'enter':
        people[name] = 1
    else:
        del(people[name])

people = sorted(people.keys(), reverse=True)
for person in people:
    print(person)
