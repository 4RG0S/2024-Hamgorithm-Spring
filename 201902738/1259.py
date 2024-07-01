import sys

while True:
    palindrome = sys.stdin.readline().strip()
    if palindrome == '0':
        break
    rev = reversed(list(palindrome))
    rev = ''.join(rev)
    if palindrome == rev:
        print('yes')
    else:
        print('no')
