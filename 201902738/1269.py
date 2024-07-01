import sys

A, B = map(int, sys.stdin.readline().strip().split())

setA = set(list(map(int, sys.stdin.readline().strip().split())))
setB = set(list(map(int, sys.stdin.readline().strip().split())))

sub_setA = setA - setB
sub_setB = setB - setA

print(len(sub_setA) + len(sub_setB))
