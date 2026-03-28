n = int(input())

# ending 0 #, ending 1 #
dp = [[] for _ in range(n)]

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp[0] = [0,1]
    dp[1] = [1,0]
    for i in range(2, n):
        dp[i] = [dp[i-1][0] + dp[i-1][1], dp[i-1][0]]

    print(sum(dp[-1]))