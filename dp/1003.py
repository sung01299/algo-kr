t = int(input())
for _ in range(t):
    n = int(input())

    zero, one = 0, 0

    dp = [[] for _ in range(n+1)]
    
    if n == 0:
        print(1, 0)
        continue
    elif n == 1:
        print(0, 1)
        continue
    else:
        dp[0] = [1,0]
        dp[1] = [0,1]
        for i in range(2, n+1):
            dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
    
    print(*dp[-1])