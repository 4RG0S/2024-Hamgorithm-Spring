import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    num = 0
    for i in range(n):
        k -= nums[i]
        if k < 0:
            num = i
            break
            
    if k >= 0:
        for i in range(n-1, -1, -1):
            k -= nums[i]
            if k < 0:
                num = i
                break
    print(num+1)
    
if __name__ == "__main__":
    main()