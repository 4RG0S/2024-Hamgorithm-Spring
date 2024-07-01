import sys

S = sys.stdin.readline().rstrip()
alphabet = [0] * 26

for s in S:
    alphabet[ord(s) - 97] += 1
    
print(' '.join(map(str, alphabet)))
