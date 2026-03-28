t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    elif n == 3:
        print(1)
    elif n == 4:
        print(2)
    elif n == 5:
        print(2)
    elif n == 6:
        print(3)
    elif n == 7:
        print(4)
    elif n == 8:
        print(5)
    else:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 2
        dp[5] = 3
        dp[6] = 4
        dp[7] = 5
        for i in range(8, n):
            dp[i] = dp[i-1] + dp[i-5]
        
        print(dp[n-1])