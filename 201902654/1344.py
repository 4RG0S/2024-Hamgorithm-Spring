A = int(input())
B = int(input())

A_percents = [0 for _ in range(20)]
B_percents = [0 for _ in range(20)]

A_percents[0] = 1
B_percents[0] = 1

for _ in range(18):
  temp = [0 for _ in range(20)]
  for i in range(19):
    temp[i] = temp[i] + A_percents[i] * ((100 - A) / 100)
    temp[i + 1] = temp[i + 1] + A_percents[i] * (A / 100)
  A_percents = temp

for _ in range(18):
  temp = [0 for _ in range(20)]
  for i in range(19):
    temp[i] = temp[i] + B_percents[i] * ((100 - B) / 100)
    temp[i + 1] = temp[i + 1] + B_percents[i] * (B / 100)
  B_percents = temp

A_get_prime_number = 0
A_get_prime_number += A_percents[2]
A_get_prime_number += A_percents[3]
A_get_prime_number += A_percents[5]
A_get_prime_number += A_percents[7]
A_get_prime_number += A_percents[11]
A_get_prime_number += A_percents[13]
A_get_prime_number += A_percents[17]

B_get_prime_number = 0
B_get_prime_number += B_percents[2]
B_get_prime_number += B_percents[3]
B_get_prime_number += B_percents[5]
B_get_prime_number += B_percents[7]
B_get_prime_number += B_percents[11]
B_get_prime_number += B_percents[13]
B_get_prime_number += B_percents[17]

print(1 - ((1 - A_get_prime_number) * (1 - B_get_prime_number)))
# print(A_percents, B_percents)
