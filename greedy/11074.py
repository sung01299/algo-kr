n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins = list(reversed(coins))

cnt = 0
for coin in coins:
    remainder = k % coin
    cnt += (k // coin)
    k = remainder

print(cnt)