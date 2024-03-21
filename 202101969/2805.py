import sys
length, want_len = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
end = max(arr)

def binary(arr, end, target):
    start = 1
    end = end

    while start <= end:
        mid = (start + end) // 2
        temp = minusAndSum(arr, mid)
        if temp >= target:
            start = mid+1
        else:
            end = mid-1
    return end
def minusAndSum(arr, num):
    s = 0
    for i in arr:
        if (i-num) > 0:
            s += (i-num)
    return s

print(binary(arr, end,want_len))
# 오답풀이 참고 : https://night-knight.tistory.com/entry/%EB%B0%B1%EC%A4%802805-%EB%82%98%EB%AC%B4%EC%9E%90%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python