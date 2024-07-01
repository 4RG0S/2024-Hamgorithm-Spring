N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

result = 0
sub_sum = [0 for _ in range(N)]
count = [0 for _ in range(M)]
sub_sum[0] = A[0] % M
for i in range(1, len(A)):
  sub_sum[i] = (sub_sum[i - 1] + A[i]) % M

sub_sum.insert(0, 0)

# print(sub_sum)
for i in range(len(sub_sum)):
  result = result + count[sub_sum[i]]
  count[sub_sum[i]] += 1

print(result)
