money = int(input())
stocks = list(map(int, input().split()))

bnp = 0
timing = 0

bnp_money = money
bnp_result = 0
for stock in stocks:
    if stock <= bnp_money:
        bnp += (bnp_money // stock)
        bnp_money -= (bnp_money // stock) * stock
bnp_result = (stocks[13] * bnp) + bnp_money
down_count = 0
up_count = 0
before_stock = 0
now_stock = 0

timing_money = money
timing_result = 0
for i in range(1, len(stocks)):
    before_stock = stocks[i-1]
    now_stock = stocks[i]

    if before_stock > now_stock:
        down_count += 1
        up_count = 0
        if down_count >= 3:
            timing += (timing_money // stocks[i])
            timing_money -= (timing_money // stocks[i]) * stocks[i]
        
    if before_stock < now_stock:
        up_count += 1
        down_count = 0
        if up_count >= 3:
            timing_money += timing * stocks[i]
            timing = 0
    if before_stock == now_stock:
        down_count = 0
        up_count = 0
timing_result = (stocks[13] * timing) + timing_money

if bnp_result > timing_result:
    print('BNP')
elif bnp_result < timing_result:
    print('TIMING')
else:
    print('SAMESAME')