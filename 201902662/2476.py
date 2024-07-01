import sys
input = sys.stdin.readline

def main():
    n = int(input())
    money = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a == b and b == c:
            money.append(10000 + a * 1000)
        elif a != b and b != c and c != a:
            money.append(max(a, b, c) * 100)
        elif a == b:
            money.append(1000 + a * 100)
        elif b == c:
            money.append(1000 + b * 100)
        elif c == a:
            money.append(1000 + c * 100)
    print(max(money))
    
if __name__ == "__main__":
    main()