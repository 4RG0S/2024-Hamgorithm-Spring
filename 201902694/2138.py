n = int(input())
cur = input()
des = input()

def light_op(n, cur, des):
    def press_switch(state, idx):
        for i in range(idx-1, idx+2):
            if 0 <= i < n:
                state[i] = '0' if state[i] == '1' else '1'
        return state
    
    def simul(initial):
        press_count = initial
        state = list(cur)
        if initial:
            press_switch(state, 0)
        for i in range(1, n):
            if state[i-1] != des[i-1]:
                press_switch(state, i)
                press_count += 1
        return press_count if state == list(des) else float('inf')

    result = min(simul(0), simul(1))
    return result if result != float('inf') else -1

min_press = light_op(n, cur, des)
print(min_press)
