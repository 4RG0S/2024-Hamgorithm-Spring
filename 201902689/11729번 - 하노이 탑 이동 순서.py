import sys
input = sys.stdin.readline

movements = []
def move(n, start, to):
    movements.append((start, to))
    return

def hanoi(n, start, to, via):
    if n == 1:
        move(1, start, to)
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n-1, via, to, start)
    return

n = int(input())
hanoi(n, 1, 3, 2)

print(len(movements))
for start, to in movements:
    print(start, to)