import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input().strip())
# A = 65
# . = 46
# chr() 함수로 ascii -> char
graph = [[0, 0] for _ in range(n+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    a, b, c = ord(a) - 64, ord(b) - 64, ord(c) - 64
    if b != -18: 
        graph[a][0] = b
    if c != -18:
        graph[a][1] = c


def prefix(node):
    if node == 0:
        return ""
    root = chr(node + 64)
    left = prefix(graph[node][0])
    right = prefix(graph[node][1])
    return root + left + right


def infix(node):
    if node == 0:
        return ""
    root = chr(node + 64)
    left = infix(graph[node][0])
    right = infix(graph[node][1])
    return left + root + right


def postfix(node):
    if node == 0:
        return ""
    root = chr(node + 64)
    left = postfix(graph[node][0])
    right = postfix(graph[node][1])
    return left + right + root


pre = prefix(1)
inf = infix(1)
post = postfix(1)

print(pre)
print(inf)
print(post)