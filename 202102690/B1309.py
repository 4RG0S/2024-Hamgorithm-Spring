n = int(input())

cur_left = 1
cur_right = 1
cur_no = 1
next_left = 0
next_right = 0
next_no = 0
for i in range(2, n+1) :
    next_left = cur_no + cur_right
    next_right = cur_no + cur_left
    next_no = cur_no + cur_left + cur_right
    cur_left = next_left
    cur_right = next_right
    cur_no = next_no

result = cur_right + cur_left + cur_no
print(result%9901)