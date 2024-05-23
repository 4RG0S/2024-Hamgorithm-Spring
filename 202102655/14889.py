# 14889번 - 스타트와 링크

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]
start = []
link = []
result = 1e9

def dfs(index, start, link):
    global result

    if index == n:
        if len(start) != n//2:
            return
        start_sum = 0
        link_sum = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                start_sum += s[start[i]][start[j]]
                link_sum += s[link[i]][link[j]]
        result = min(result, abs(start_sum - link_sum))
        return

    start.append(members[index])
    dfs(index+1, start, link)
    start.pop()

    link.append(members[index])
    dfs(index+1, start, link)
    link.pop()

dfs(0, start, link)
print(result)
