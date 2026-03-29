'''
dp[i][j] = i번째 동전까지 썼을때 j원을 만드는 방법의 수

i번째 동전을 0개 쓴 경우: D[i-1][j]
i번째 동전을 1개 이상 쓴 경우: D[i-1][j-c[i]]
dp[i][j] = d[i-1][j] + d[i][j-c[i]]
'''

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [[0 for _ in range(m+1)] for _ in range(len(coins))]

    for i in range(len(coins)):
        dp[i][0] = 1

    for i in range(len(coins)):
        for j in range(1, m + 1):
            if i - 1 >= 0:
                dp[i][j] += dp[i-1][j] 
            if j - coins[i-1] >= 0:
                dp[i][j] += dp[i][j-coins[i-1]]

    print(dp[-1][-1])