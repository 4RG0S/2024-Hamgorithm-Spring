import sys

def get_z_index(S: str):
  z_index = [0 for _ in range(len(S))]
  left = 0
  right = 0
  for i in range(1, len(S)):
    if right < i:
      left = right = i
      while right < len(S) and S[right] == S[right - left]:
        right += 1
      z_index[i] = right - left
      right -= 1
    else:
      k = i - left
      if z_index[k] < right - i + 1:
        z_index[i] = z_index[k]
      else:
        left = i
        while right < len(S) and S[right] == S[right - left]:
          right += 1
        z_index[i] = right - left
        right -= 1
  return z_index

S = sys.stdin.readline().strip()
M = int(sys.stdin.readline())
reversed_S = S[::-1]
z_index = get_z_index(reversed_S)
z_index[0] = len(S)
for i in range(M):
  i = int(sys.stdin.readline())
  print(z_index[len(S) - i])
