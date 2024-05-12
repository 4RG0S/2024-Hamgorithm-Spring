S = input()
S_lst = []

for _ in S:
    S_lst.append(S)
    S = S[1:]

for i in sorted(S_lst):
    print(i)