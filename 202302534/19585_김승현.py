import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.child = {}
        self.check = False

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        cur.count += 1
        l=len(string)
        for i in range(l):
            c = string[i]
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.count += 1
            if i == l-1:
                cur.check = True


    def search(self, string):
        cur = self.head
        S = set()
        cnt = 0

        for c in string:
            cnt += 1
            if c in cur.child:
                cur = cur.child[c]
                if cur.check:
                    S.add(cnt)
            else:
                return S

        if cur.data:
            return S
        else:
            return S


trie = Trie()
n, m = map(int, input().split())
tmp = []
S =set()
for _ in range(n):
    A = input().rstrip()
    tmp.append(A)

for _ in range(m):
    B = input().rstrip()
    S.add(B)
for _ in tmp:  # color
    trie.insert(_)

k=int(input())
for _ in range(k):
    ss = input().rstrip()
    L =len(ss)
    S1 =trie.search(ss)
    flag = True
    for i in S1:
        if ss[i:] in S:
            print("Yes")
            flag =False
            break
    if flag:
        print("No")
