## join !!
'''
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. 
(1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
'''
import sys

N = int(sys.stdin.readline())
numbers= sys.stdin.readline().rstrip().split()
operators = list(map(int, sys.stdin.readline().split()))
operator_dic = {0:'+', 1:'-', 2:'*', 3:'/'} # key값은 operators의 인덱스값
can_use = operators[:]
min_result = 10**10
max_result = -10**10

def calc(num1, operator, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+': return num1+num2
    elif operator == '-': return num1-num2
    elif operator == '*': return num1*num2
    elif operator == '/':
        if num1 < 0 or num2 < 0:
            # 음수 나눗셈인 경우, 양수로 바꿔 나눗셈한뒤 몫에 음수 취하기
            return -int(abs(num1)//abs(num2))
        else: return int(num1//num2)
    
def put(idx, result, numbers, can_use):
    # idx는 몇번째 number까지 계산했는가.
    global min_result, max_result
    # print(idx, len(expression))
    if idx == len(numbers)-1:
        # 식 계산값으로 최대 최소값 업데이트
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    # 다음 빈 칸에 대해 탐색
    for operator_idx in range(4):
        can_use_1 = can_use[:]
        if can_use_1[operator_idx] > 0:
            calc_result = calc(result, operator_dic[operator_idx], numbers[idx+1])
            can_use_1[operator_idx] -= 1
            put(idx+1, calc_result, numbers[:], can_use_1)
            
put(0, numbers[0], list(numbers), can_use)
print(max_result)
print(min_result)