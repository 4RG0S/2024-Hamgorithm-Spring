import sys
input = sys.stdin.readline

def sub_sum():
    start, end = 0, 0
    total = 0
    min_length = 1e9
    while True:
        if total >= s:
            min_length = min(min_length, end - start)
            total -= sequence[start]
            start += 1
        elif end == n:
            break
        else:
            total += sequence[end]
            end += 1
    if min_length == 1e9:
        print(0)
    else:
        print(min_length)

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
sub_sum()