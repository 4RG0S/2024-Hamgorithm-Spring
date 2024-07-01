import sys

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_ = sys.maxsize

while True:
    if sum >= S:
        min_ = min(min_, right-left)
        sum -= nums[left]
        left +=1
    elif right == N:
        break
    else:
        sum += nums[right]
        right += 1

if min_ == sys.maxsize:
    print(0)
else:
    print(min_)