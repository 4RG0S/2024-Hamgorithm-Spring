import sys

n, m = map(int, input().split())
sequence = [int(input()) for _ in range(n)]
sequence.sort()

left, right = 0, 0
min_difference = float('inf')

while left < n and right < n:
    if sequence[right] - sequence[left] >= m:
        min_difference = min(min_difference, sequence[right] - sequence[left])
        left += 1
    else:
        right += 1

print(min_difference)
