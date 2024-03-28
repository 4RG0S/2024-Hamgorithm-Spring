import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
def find_num (arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end )//2
        if arr[mid] == target:
            return True
        elif arr[mid] <= target:
            start = mid +1
        elif arr[mid] > target:
            end = mid -1

for i in M_list:
    result = find_num(N_list, i)
    if result:
        print(1)
    else:
        print(0)