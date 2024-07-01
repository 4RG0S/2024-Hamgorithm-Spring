import sys
input = sys.stdin.readline

word = input().rstrip()
count = [0] * 26

for w in word:
    cal = ord(w)-65
    if cal > 25:
        count[cal-32] += 1
    else:
        count[cal] += 1

if count.count(max(count)) > 1:
    print("?")
else:
    print(chr(count.index(max(count))+65))