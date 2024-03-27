from collections import deque

def main():
    n = int(input())
    que = deque()

    def program():
        length = len(que)
        if length == n:
            return 1
        
        line = [False for _ in range(n)]
        for i, v in enumerate(que):
            line[v] = True
            if v + length - i < n:
                line[v + length - i] = True
            if v - length + i >= 0:
                line[v - length + i] = True

        cnt = 0
        for i in range(n):
            if line[i]:
                continue
            que.append(i)
            cnt += program()
            que.pop()
        return cnt
    
    print(program())


if __name__ == "__main__":
    main()