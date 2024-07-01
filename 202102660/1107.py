import sys

# 1. 번호 + (+,-) 눌러서 만들때 click 수 (-> 번호만 누르는 경우도 포함 됨)
    # 일단 그냥 +-1씩 해보면서 모든 자리수가 available한 경우 멈추기로 ㄱㄱ 
# 2. +, - 만 눌러서 만들때 click 수

want = int(sys.stdin.readline())
broken_num = int(sys.stdin.readline().strip())
if broken_num != 0:
    broken = list(map(int, sys.stdin.readline().split()))
else:
    broken = []
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def calc_1(want, click_calc_2):

    under_click, upper_click = sys.maxsize, sys.maxsize

    under, upper = want, want

    i = 0
    while(True):
        under_available = True

        under = want - i
        if under < 0 or click_calc_2 <= (len(str(under))+abs(under - want)):
            break
        for str_num in str(under):
            if int(str_num) in broken:
                under_available = False

        if under_available:
            under_click = (len(str(under))+abs(under - want))
            break
    
        i += 1

    i = 0
    while(True):
        upper_available = True
        upper = want + i
        # TODO: upper로 계산한 click수보다 under, calc2가 더 작으면 멈추기 
        if (len(str(upper))+abs(upper - want)) >= click_calc_2 or (len(str(upper))+abs(upper - want)) >= under_click:
            break

        for str_num in str(upper):
            if int(str_num) in broken:
                upper_available = False

        if upper_available:
            upper_click = (len(str(upper))+abs(upper - want))
            break
        i += 1
    
    return under_click, upper_click

def calc_2(want):
    return abs(want - 100)

calc_2_click = calc_2(want)
under_click, upper_click = calc_1(want, calc_2_click)

print(min(calc_2_click, under_click, upper_click))