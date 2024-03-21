import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        n = int(input())
        hasTeam = [0 for _ in range(n+1)]
        visit = [False for _ in range(n+1)]
        choice = [0] + list(map(int, input().split()))
        
        for i in range(1, n+1):
            if visit[i]:
                continue
            
            crnt = i
            while visit[crnt] == False:
                visit[crnt] = True
                crnt = choice[crnt]
                
            while hasTeam[crnt] == 0:
                hasTeam[crnt] = 1
                crnt = choice[crnt]
        
            crnt = i
            while hasTeam[crnt] == 0:
                hasTeam[crnt] = 2
                crnt = choice[crnt]
        
        cnt = n
        for i in range(1, n+1):
            if hasTeam[i] == 1:
                cnt -= 1
        print(cnt)
    
if __name__ == "__main__":
    main()