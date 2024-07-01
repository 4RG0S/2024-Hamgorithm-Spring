n = int(input())
nums = list(map(int, input().split()))
s = int(input())

count = 0
low = 0
if n > s :
    cur_s = s
else :
    cur_s = n-1

sorted_arr = sorted(nums, reverse=True)

while count < s :
    max_index = low
    for i in range(low, cur_s+1) :
        if nums[max_index] < nums[i] :
            max_index = i

    for i in range(max_index, low, -1) :
        nums[i], nums[i-1] = nums[i-1], nums[i]
        count+=1
        if count == s :
            break
    
    if nums == sorted_arr :
        break

    low += 1
    cur_s = low + s-count
    if n <= cur_s :
        cur_s = n-1
    
print(*nums)

