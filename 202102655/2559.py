N, K = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = sum(nums[0:K])
sum_cnt = max_sum
for i in range(K, N):
    sum_cnt -= nums[i-K]
    sum_cnt += nums[i]
    if sum_cnt > max_sum:
        max_sum = sum_cnt
print(max_sum)