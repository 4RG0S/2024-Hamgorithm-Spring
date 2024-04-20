import sys

while True:
    data = list(map(str, sys.stdin.readline().split()))
    if data[0] == "#":
        break

    name, age, weight = data[0], int(data[1]), int(data[2])

    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')
