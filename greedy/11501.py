import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    max_price = prices[-1]
    profit = 0
    for i in range(len(prices)-1, -1, -1):
        max_price = max(max_price, prices[i])
        profit += (max_price - prices[i])
    
    print(profit)
    