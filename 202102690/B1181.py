n = int(input())
words = []
for _ in range(n) :
    cur_word = input()
    if cur_word not in words :
        words.append(cur_word)

words.sort()
words.sort(key = len)
for i in words :
    print(i)