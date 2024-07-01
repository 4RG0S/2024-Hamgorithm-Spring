import sys

sentence = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
final = []

for s in sentence:
    #  한 글자씩 추가하면서 비교
    final.append(s)
    if s == target[-1] and len(final) >= len(target):
        # target과 비교
        if final[-len(target):] == list(target):
            for _ in range(len(target)):
                final.pop() # 잘라내기

if final:
    print("".join(final))
else: print("FRULA")
