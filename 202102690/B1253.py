n = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = 0

for i in range(n) :
    cur_num = nums[i]
    low = 0
    high = n-1
    while low < high :
        if nums[low] + nums[high] == cur_num :
            if low == i :
                low += 1
            elif high == i :
                high -= 1
            else :
                result += 1
                break
        elif nums[low] + nums[high] > cur_num :
            high -= 1
        else :
            low += 1

print(result)

# for i, a in enumerate(nums) :
#     new_nums = copy.deepcopy(nums)
#     new_nums.pop(i)
#     for j, b in enumerate(new_nums) :
#         cur_nums = copy.deepcopy(new_nums)
#         cur_nums.pop(j)
#         if a - b in cur_nums :
#             result += 1
#             break

# print(result)

