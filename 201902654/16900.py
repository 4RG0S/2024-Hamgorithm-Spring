line = list(input().split())
S = line[0]
K = int(line[1])

def get_z_index(S):
    z_index = [0] * len(S)
    left = 0
    right = 0
    for i in range(1, len(S)):
        if i > right:
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

z_index = get_z_index(S)
last_duplicated_value = 0
for i in range(len(S)):
    index = len(S) - i - 1
    if z_index[index] > 0 and z_index[index] == i + 1:
      last_duplicated_value = z_index[index]
left_string_length = len(S) - last_duplicated_value
print(left_string_length * K + last_duplicated_value)
