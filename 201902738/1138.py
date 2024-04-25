import sys

N = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().strip().split(' ')))
people.reverse()

height = []
for i in range(N, 0, -1):
    k = people[N - i]
    # print('i:', i, 'k:', k)
    height.insert(k, i)
    
print(' '.join(map(str, height)))
