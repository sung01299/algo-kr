n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [[float('inf') for _ in range(k+1)] for _ in range(len(coins))]


for i in range(len(coins)):
    dp[i][0] = 0
    for j in range(1, k+1):
        if i-1 >= 0:
            dp[i][j] = dp[i-1][j]
        if j - coins[i] >= 0:
            dp[i][j] = min(dp[i][j], dp[i][j-coins[i]] + 1)

print(dp[-1][-1] if dp[-1][-1] != float('inf') else -1)
    