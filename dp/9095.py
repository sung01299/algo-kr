t = int(input())

for _ in range(t):
    n = int(input())

    dp = [0 for _ in range(n+1)]

    dp[1] = 1
    if n > 1:
        dp[2] = 1
    if n > 2:
        dp[3] = 1

    for i in range(2, n+1):
        dp[i] += dp[i-1]
        if i > 2:
            dp[i] += dp[i-2]
        if i > 3:
            dp[i] += dp[i-3]
    
    print(dp[-1])