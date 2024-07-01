from collections import deque

K, N = list(map(int, input().split()))
num_str = input()
queue = deque()

queue.append(int(num_str[0]))
for i in range(1, K):
  val = int(num_str[i])
  while len(queue) > 0 and queue[len(queue) - 1] < val and N > 0:
    queue.pop()
    N -= 1
  queue.append(val)

for _ in range(N):
  queue.pop()

for i in range(len(queue)):
  print(queue[i], end='')
